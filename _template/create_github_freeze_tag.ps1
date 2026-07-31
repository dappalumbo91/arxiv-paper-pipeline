param(
  [string]$RepoRoot = "",
  [string]$Commit = "",
  [string]$Tag = "",
  [switch]$Push
)
# Fill from FREEZE.yaml before use.
$ErrorActionPreference = "Stop"
if (-not $RepoRoot -or -not $Commit -or -not $Tag) {
  Write-Host "Usage: .\create_github_freeze_tag.ps1 -RepoRoot path -Commit sha -Tag vX.Y-arxiv-paperNN [-Push]"
  exit 1
}
Set-Location $RepoRoot
git rev-parse "$Commit^{commit}" | Out-Null
git tag -a $Tag $Commit -m "arXiv freeze $Tag"
Write-Host "Created tag $Tag -> $Commit"
if ($Push) { git push origin $Tag; Write-Host "Pushed $Tag" }
