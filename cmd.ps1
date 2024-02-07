New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" -Name %USERPROFILE%\run.bat -Value RUNASADMIN -PropertyType string -Force | Out-Null
