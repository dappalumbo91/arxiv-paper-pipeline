# Create and push the arXiv paper freeze tag on FSOT-2.1-Lean.
# Run from a clean clone of the repo, or set $RepoRoot.

param(
  [string]$RepoRoot = "I:\FSOT-Physical-Archive\02_FSOT-2.1-Lean-Full",
  [string]$Commit = "81bc89364d206aca6da4c65f3faa875ad168cc8e",
  [string]$Tag = "v2.6-arxiv-paper01",
  [switch]$Push
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

Write-Host "Repo:  $(Get-Location)"
Write-Host "Commit:$Commit"
Write-Host "Tag:   $Tag"

git rev-parse "$Commit^{commit}" | Out-Null
git tag -a $Tag $Commit -m "arXiv paper 01: formal scalar engine + contested cosmology freeze (2026-07-16)"

Write-Host "Created local tag $Tag -> $Commit"
if ($Push) {
  git push origin $Tag
  Write-Host "Pushed $Tag to origin"
} else {
  Write-Host "Dry run complete. Re-run with -Push to push to GitHub:"
  Write-Host "  .\create_github_freeze_tag.ps1 -Push"
}
