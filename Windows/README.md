# This folder is used to organize various tools for Windows

### 1. Install OpenSSH tools for VSCode deployment plugin
Open Windows PowerShell or Command Prompt as administrator

    Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH.Client*' | Add-WindowsCapability -Online
After completion, enter VSCode to install the plugin

    Remote-SSH
    Remote-Development
    Remote-Explorer
### 2. Public network IP address query
Overseas address inquiry

    curl ipinfo.io/ip
Local address lookup

    curl -L ip.tool.lu
### 3. Process management
View open ports

    netstat -ant
    netstat -ano
    netstat -p tcp -a
    netstat -p udp -a
    netstat -p tcp -a | findstr 80
    netstat -p tcp -a | findstr 80
Manager

    netstat -b -o 4709
    tasklist /FI "PID eq 1136"
    taskkill /f /pid 1136
    taskkill /im chrome*
    