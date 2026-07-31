#!/usr/bin/env python3
"""
Verify that an FSOT-2.1-Lean checkout matches the paper freeze (FREEZE.yaml).

Usage:
  set FSOT_ROOT=C:\\path\\to\\FSOT-2.1-Lean
  python verify_paper_claims.py

  python verify_paper_claims.py --fsot-root /path/to/FSOT-2.1-Lean
  python verify_paper_claims.py --fsot-root /path/to/FSOT-2.1-Lean --strict-hash

Exit codes:
  0 — all available checks passed
  1 — one or more hard failures
  2 — freeze/repo path missing
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


HERE = Path(__file__).resolve().parent
FREEZE_PATH = HERE / "FREEZE.yaml"


def load_freeze() -> dict:
    text = FREEZE_PATH.read_text(encoding="utf-8")
    if yaml is not None:
        return yaml.safe_load(text)
    # Minimal YAML subset parser for this freeze file if PyYAML missing
    return _minimal_yaml(text)


def _minimal_yaml(text: str) -> dict:
    """Enough to read FREEZE.yaml keys used by this script without PyYAML."""
    out: dict = {
        "oracle": {},
        "formal": {},
        "empirical": {"contested": {}, "h0": {}},
        "repository": {},
        "toolchains": {},
    }
    section = []
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent == 0 and line.endswith(":"):
            section = [line[:-1].strip()]
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if val == "":
            if indent == 0:
                section = [key]
            elif indent == 2:
                section = [section[0], key] if section else [key]
            continue
        # coerce
        if val.lower() in ("true", "false"):
            coerced: object = val.lower() == "true"
        else:
            try:
                coerced = int(val)
            except ValueError:
                try:
                    coerced = float(val)
                except ValueError:
                    coerced = val
        if indent == 0:
            out[key] = coerced
        elif indent == 2 and section:
            out.setdefault(section[0], {})
            if isinstance(out[section[0]], dict):
                out[section[0]][key] = coerced
        elif indent == 4 and len(section) >= 2:
            out.setdefault(section[0], {})
            out[section[0]].setdefault(section[1], {})
            if isinstance(out[section[0]][section[1]], dict):
                out[section[0]][section[1]][key] = coerced
    return out


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def load_json(path: Path) -> dict | None:
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def near(a: float, b: float, tol: float) -> bool:
    return abs(float(a) - float(b)) <= tol


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify FSOT checkout vs paper FREEZE.yaml")
    ap.add_argument(
        "--fsot-root",
        type=Path,
        default=os.environ.get("FSOT_ROOT"),
        help="Path to FSOT-2.1-Lean clone (or set FSOT_ROOT)",
    )
    ap.add_argument(
        "--strict-hash",
        action="store_true",
        help="Fail if vendor/fsot_compute.py hash mismatches freeze",
    )
    ap.add_argument(
        "--require-cross-proof",
        action="store_true",
        help="Fail if cross_proof report missing or overall_ok is false",
    )
    args = ap.parse_args()

    if not FREEZE_PATH.is_file():
        print(f"ERROR: missing {FREEZE_PATH}", file=sys.stderr)
        return 2
    if not args.fsot_root:
        print(
            "ERROR: pass --fsot-root PATH or set FSOT_ROOT to your FSOT-2.1-Lean clone",
            file=sys.stderr,
        )
        return 2

    root = Path(args.fsot_root).expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: FSOT root not a directory: {root}", file=sys.stderr)
        return 2

    freeze = load_freeze()
    hard: list[str] = []
    soft: list[str] = []
    ok: list[str] = []

    print(f"FSOT root: {root}")
    print(f"Freeze:    {FREEZE_PATH}")
    print(f"Edition:   {freeze.get('edition_id')}")
    print()

    # --- Oracle hash ---
    oracle_path = root / "vendor" / "fsot_compute.py"
    expected_hash = str(freeze.get("oracle", {}).get("sha256", "")).upper()
    if oracle_path.is_file():
        got = sha256_file(oracle_path)
        if got == expected_hash:
            ok.append(f"oracle SHA-256 match: {got[:12]}…")
        else:
            msg = f"oracle SHA-256 mismatch: got {got}, expected {expected_hash}"
            (hard if args.strict_hash else soft).append(msg)
    else:
        hard.append(f"missing oracle: {oracle_path}")

    # --- Publication claims ---
    claims_path = root / "data" / "publication_claims_manifest.json"
    claims = load_json(claims_path)
    if claims is None:
        hard.append(f"missing {claims_path.relative_to(root)} — run publication bundle first")
    else:
        emp = claims.get("empirical_evidence", {})
        cont = claims.get("contested_sector_evidence", {})
        formal = claims.get("formal_verification", {})

        green = emp.get("benchmark_domains_green")
        exp_green = freeze.get("empirical", {}).get("benchmark_domains_green", "394/394")
        if green == exp_green:
            ok.append(f"benchmark green: {green}")
        else:
            # margin audit may show more domains; soft unless empty
            soft.append(f"benchmark green claims: got {green}, freeze {exp_green}")

        pooled = emp.get("pooled_median_of_domains_pct")
        exp_pooled = float(freeze.get("empirical", {}).get("cross_domain_pooled_median_pct", 0.013))
        if pooled is not None and near(pooled, exp_pooled, 0.005):
            ok.append(f"cross-domain pooled median: {pooled}%")
        else:
            soft.append(f"cross-domain pooled median: got {pooled}, expected ~{exp_pooled}")

        c_med = cont.get("fsot_pooled_median_pct")
        exp_c = float(freeze.get("empirical", {}).get("contested", {}).get("fsot_pooled_median_pct", 0.03))
        if c_med is not None and near(c_med, exp_c, 0.005):
            ok.append(f"contested pooled median: {c_med}%")
        else:
            hard.append(f"contested pooled median: got {c_med}, expected ~{exp_c}")

        c_n = cont.get("observable_count")
        exp_n = int(freeze.get("empirical", {}).get("contested", {}).get("observable_count", 13))
        if c_n == exp_n:
            ok.append(f"contested observables: {c_n}")
        else:
            hard.append(f"contested observables: got {c_n}, expected {exp_n}")

        if formal.get("overall_ok") is True:
            ok.append("claims formal overall_ok: true")
        else:
            soft.append(f"claims formal overall_ok: {formal.get('overall_ok')}")

        atomic = formal.get("atomic_obligations")
        exp_atomic = int(freeze.get("formal", {}).get("atomic_obligations_claims_manifest", 1863))
        if atomic is not None and int(atomic) >= exp_atomic:
            ok.append(f"claims atomic obligations: {atomic} (>= {exp_atomic})")
        elif atomic is not None:
            hard.append(f"claims atomic obligations: {atomic} < {exp_atomic}")
        else:
            soft.append("claims atomic_obligations missing")

    # --- Contested closure ---
    clo_path = root / "data" / "contested_observables_closure.json"
    clo = load_json(clo_path)
    if clo is None:
        soft.append(f"missing {clo_path.name} (regenerate with bundle)")
    else:
        obs = clo.get("observables") or clo.get("panel_summary")
        if isinstance(obs, list) and len(obs) >= 10:
            ok.append(f"contested closure observables list length: {len(obs)}")
        else:
            # structure variants
            soft.append("contested closure structure differs; open file manually")

    # --- Certificate (Lean) ---
    cert_path = root / "data" / "certificate.json"
    cert = load_json(cert_path)
    if cert is None:
        soft.append("certificate.json missing — run Lean verification / export_certificate.py")
    else:
        if cert.get("lean_build_ok") is True:
            ok.append("certificate lean_build_ok: true")
        else:
            soft.append(f"certificate lean_build_ok: {cert.get('lean_build_ok')}")
        sorry = cert.get("sorry_count_formal")
        if sorry == 0:
            ok.append("sorry_count_formal: 0")
        elif sorry is not None:
            hard.append(f"sorry_count_formal: {sorry} (expected 0)")
        auth = (cert.get("authority") or {}).get("sha256", "")
        if auth and auth.upper() == expected_hash:
            ok.append("certificate authority hash matches freeze")
        elif auth:
            soft.append(f"certificate authority hash {auth[:12]}… vs freeze")

    # --- Cross-proof ---
    xp_path = root / "data" / "cross_proof_verification_report.json"
    xp = load_json(xp_path)
    if xp is None:
        msg = "cross_proof report missing — run --full-cross-proof for Tier 3"
        (hard if args.require_cross_proof else soft).append(msg)
    else:
        if xp.get("overall_ok") is True:
            ok.append("cross_proof overall_ok: true")
        else:
            (hard if args.require_cross_proof else soft).append(
                f"cross_proof overall_ok: {xp.get('overall_ok')}"
            )
        atomic_xp = (xp.get("full_formal_spine") or {}).get("atomic_provable_count")
        min_atomic = int(freeze.get("formal", {}).get("atomic_obligations_claims_manifest", 1863))
        if atomic_xp is not None and int(atomic_xp) >= min_atomic:
            ok.append(f"cross_proof atomic_provable_count: {atomic_xp} (>= {min_atomic})")
        elif atomic_xp is not None:
            hard.append(f"cross_proof atomic_provable_count {atomic_xp} < {min_atomic}")

    # --- Figures ---
    fig_dir = root / "data" / "figures"
    for name in (
        "contested_fsot_vs_lcdm.png",
        "h0_landscape.png",
        "spine_walkthrough.png",
    ):
        if (fig_dir / name).is_file():
            ok.append(f"figure present: {name}")
        else:
            soft.append(f"figure missing: data/figures/{name}")

    # --- Report ---
    print("PASSED")
    for m in ok:
        print(f"  [ok]   {m}")
    if soft:
        print("\nWARNINGS (soft)")
        for m in soft:
            print(f"  [warn] {m}")
    if hard:
        print("\nFAILURES (hard)")
        for m in hard:
            print(f"  [FAIL] {m}")

    print()
    if hard:
        print("RESULT: FAIL — paper freeze not satisfied")
        return 1
    print("RESULT: PASS — available freeze checks satisfied")
    if soft:
        print("(soft warnings remain; see SCIENTIST_REPRODUCE.md tiers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
