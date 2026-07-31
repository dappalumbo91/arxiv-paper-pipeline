# Build topic-named PDF: {basename}.tex -> {basename}.pdf
# Never leave the deliverable named only "paper.pdf".
param(
  [string]$Basename = ""
)

$ErrorActionPreference = "Stop"
$here = $PSScriptRoot
if (-not $here) { $here = (Get-Location).Path }

if (-not $Basename) {
  $mbFile = Join-Path $here "manuscript_basename.txt"
  if (Test-Path $mbFile) {
    $Basename = (Get-Content $mbFile -Raw).Trim()
  } else {
    $Basename = Split-Path $here -Leaf
  }
}

$tex = Join-Path $here ($Basename + ".tex")
if (-not (Test-Path $tex)) {
  $legacy = Join-Path $here "paper.tex"
  if (Test-Path $legacy) {
    Write-Host "Renaming legacy paper.tex to $Basename.tex"
    Rename-Item -Path $legacy -NewName ($Basename + ".tex")
    $tex = Join-Path $here ($Basename + ".tex")
  } else {
    throw "Missing TeX source: $tex"
  }
}

Set-Content -Path (Join-Path $here "manuscript_basename.txt") -Value $Basename -Encoding ascii -NoNewline

Write-Host "Building $Basename.pdf from $Basename.tex"
Push-Location $here
try {
  & pdflatex -interaction=nonstopmode ($Basename + ".tex") | Out-Null
  if (Test-Path ($Basename + ".aux")) {
    & bibtex $Basename 2>$null | Out-Null
  }
  & pdflatex -interaction=nonstopmode ($Basename + ".tex") | Out-Null
  & pdflatex -interaction=nonstopmode ($Basename + ".tex") | Out-Null
} finally {
  Pop-Location
}

$pdf = Join-Path $here ($Basename + ".pdf")
if (-not (Test-Path $pdf)) {
  throw "Build failed: $pdf not found"
}
Write-Host "OK: $pdf"
Get-Item $pdf | Format-List FullName, Length, LastWriteTime
