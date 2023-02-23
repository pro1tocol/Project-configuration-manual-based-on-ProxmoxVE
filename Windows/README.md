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

    
