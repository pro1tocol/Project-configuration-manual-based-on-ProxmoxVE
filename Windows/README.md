# This folder is used to organize various tools for Windows

### 1. Install tools
Open Windows PowerShell or Command Prompt as administrator

    Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH.Client*' | Add-WindowsCapability -Online
Chocolatey

    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

### 2. Public network IP address query
Overseas address inquiry

    curl ipinfo.io/ip
Local address lookup

    curl -L ip.tool.lu
### 3. Process management
View open ports

    netstat -ant
    netstat -ano
    netstat -p tcp -ano
    netstat -p tcp -a
    netstat -p udp -a
    netstat -p tcp -a | findstr 80
    netstat -p tcp -a | findstr 80
Manager

    netstat -b -o 4709
    tasklist /FI "PID eq 1136"
    taskkill /f /pid 1136
    taskkill /im chrome*
### 4. Optimization

High contrast setting(水生/沙漠)

<div align="center">
    
| main color  | secondary color| connecting color|
| ---------- | -----------| -----------|
| R:100<br>G:210<br>B:255   | R:0<br>G:0<br>B:0   | R:30<br>G:30<br>B:30   |

</div>

Change tpye

    Win+R
    regedit
    
    ..\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layouts\00000804 #Chinese
    [Layout File] KBDUS.DLL to KBDUK.DLL
    [Layout Text] US Keyboard to UK Keyboard
Install python

    ..\python.exe -m pip install --upgrade pip
    Win+R
    sysdm.cpl > advanced > environment variable
    pip list
Install winfetch

    Get-ExecutionPolicy
    > Restricted or RemoteSigned
    Set-ExecutionPolicy RemoteSigned
Install Ntop

    choco install NTop.Portable
    ntop
Install VIM

    download gvim90.exe
    Win+R
    sysdm.cpl > advanced > environment variable
    Vim  > /local/address
    path > %Vim%
Install Nmap

    Win+R
    sysdm.cpl > advanced > environment variable
    Nmap  > C:\Program Files (x86)\Nmap
    path > %Nmap%
Install Git

    choco install git
Install Android

    Win+R
    sysdm.cpl > advanced > environment variable
    Android  > /local/address
    path > %Android%
