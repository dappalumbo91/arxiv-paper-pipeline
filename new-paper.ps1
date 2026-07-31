<#
.SYNOPSIS
  Scaffold a new arXiv paper package from the standardized template.

.EXAMPLE
  .\new-paper.ps1 -Slug "02-fuels-formal" -Title "FSOT Fuel Lab Formal Readouts"
.EXAMPLE
  .\new-paper.ps1 -Number 3 -Slug "lean-sign-certificates" -Title "..." -Author "Damian Arthur Palumbo"
#>
param(
  [Parameter(Mandatory = $true)]
  [string]$Slug,

  [Parameter(Mandatory = $true)]
  [string]$Title,

  [int]$Number = 0,

  [string]$Author = "Damian Arthur Palumbo",

  [string]$RepoUrl = "",

  [string]$PrimaryCategory = "cs.LO",

  [string]$Root = ""
)

$ErrorActionPreference = "Stop"

if (-not $Root) {
  if ($PSScriptRoot) { $Root = $PSScriptRoot }
  else { $Root = Split-Path -Parent $MyInvocation.MyCommand.Path }
}
if (-not $Root) { $Root = "C:\Users\damia\Desktop\arxiv-papers" }
$Root = (Resolve-Path $Root).Path

# Normalize slug: allow "02-foo" or "foo"
$slug = $Slug.Trim().ToLower() -replace '[^a-z0-9\-]+', '-' -replace '-+', '-' -replace '^-|-$', ''
if ($Number -gt 0 -and $slug -notmatch '^\d{2}-') {
  $slug = ("{0:D2}" -f $Number) + "-" + $slug
}
if ($slug -notmatch '^\d{2}-') {
  # auto-next number
  $existing = Get-ChildItem $Root -Directory | Where-Object { $_.Name -match '^\d{2}-' }
  $max = 0
  foreach ($d in $existing) {
    if ($d.Name -match '^(\d{2})-') {
      $n = [int]$Matches[1]
      if ($n -gt $max) { $max = $n }
    }
  }
  $slug = ("{0:D2}" -f ($max + 1)) + "-" + $slug
}

$dest = Join-Path $Root $slug
$template = Join-Path $Root "_template"
if (-not (Test-Path $template)) {
  throw "Template not found: $template"
}
if (Test-Path $dest) {
  throw "Already exists: $dest"
}

Write-Host "Scaffolding $dest"
Copy-Item -Path $template -Destination $dest -Recurse -Force

# Token replace in text files
$today = Get-Date -Format "yyyy-MM-dd"
$replacements = @{
  "{{TITLE}}"            = $Title
  "{{AUTHOR}}"           = $Author
  "{{SLUG}}"             = $slug
  "{{DATE}}"             = $today
  "{{REPO_URL}}"         = $(if ($RepoUrl) { $RepoUrl } else { "https://github.com/OWNER/REPO" })
  "{{PRIMARY_CATEGORY}}" = $PrimaryCategory
  "{{PAPER_DIR}}"         = $dest
}

$exts = @("*.md", "*.txt", "*.yaml", "*.yml", "*.tex", "*.ps1", "*.py", "*.bib")
Get-ChildItem $dest -Recurse -File -Include $exts | ForEach-Object {
  $text = Get-Content $_.FullName -Raw -ErrorAction SilentlyContinue
  if ($null -eq $text) { return }
  $orig = $text
  foreach ($k in $replacements.Keys) {
    $text = $text.Replace($k, $replacements[$k])
  }
  if ($text -ne $orig) {
    Set-Content -Path $_.FullName -Value $text -Encoding utf8 -NoNewline
  }
}

# Ensure dirs
foreach ($sub in @("figures", "logs", "arxiv_upload", "arxiv_upload\figures", "arxiv_upload\anc", "anc")) {
  New-Item -ItemType Directory -Path (Join-Path $dest $sub) -Force | Out-Null
}

Write-Host ""
Write-Host "Created: $dest"
Write-Host "Next:"
Write-Host "  1. Edit FREEZE.yaml with real pins from your source repo"
Write-Host "  2. In Grok Build: /arxiv-paper  (or open PLAYBOOK.md)"
Write-Host "  3. Clean-clone verify before final prose freeze"
Write-Host ""
Write-Host "Playbook: $(Join-Path $Root 'PLAYBOOK.md')"
