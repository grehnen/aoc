param (
    [string]$targetFolder
)

# Ensure the target folder exists
if (-Not (Test-Path -Path $targetFolder)) {
    Write-Host "Target folder does not exist."
    exit 1
}

# Get all files in the templates directory
$templateFiles = Get-ChildItem -Path .\templates -File

# Create symbolic links for each file in the target folder
foreach ($file in $templateFiles) {
    $linkPath = Join-Path -Path $targetFolder -ChildPath $file.Name
    New-Item -ItemType SymbolicLink -Path $linkPath -Target $file.FullName
    Write-Host "Created symlink: $linkPath -> $file.FullName"
}