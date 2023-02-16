#!/usr/bin/env -S pwsh -nop
<#
.EXAMPLE
scripts/shared.ps1
#>
$ErrorActionPreference = 'Stop'
try {
    Get-ChildItem Function:\ConvertTo-PEM
} catch {
    $common = 'https://raw.githubusercontent.com/szymonos/ps-modules/main/modules/do-common/Functions/common.ps1'
    Invoke-Expression $([Net.WebClient]::new().DownloadString($common))
}

Get-ChildItem Function:\ConvertTo-PEM
