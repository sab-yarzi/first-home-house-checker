if (Test-Path "./secrets.ps1") {
    . ./secrets.ps1
} else {
    Write-Error "secrets.ps1 file not found. Please create the file with necessary secrets."
    exit 1
}



if (-not (Get-Command doctl -ErrorAction SilentlyContinue)) {
    Write-Error "doctl not found."
    exit 1
}

doctl serverless deploy . --verbose
if ($LASTEXITCODE -ne 0) {
    Write-Error "Deployment failed."
    exit $LASTEXITCODE
}
Write-Output "Deployment succeeded."

