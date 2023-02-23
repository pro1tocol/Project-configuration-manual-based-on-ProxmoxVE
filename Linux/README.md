# Linux common settings and tools

### 1. Daily configuration
modify time zone

    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
Language setting

    #debian
    sudo apt install xfonts-intl-chinese xfonts-wqy fonts-noto-cjk
    #archlinux
    sudo pacman -S adobe-source-han-serif-cn-fonts wqy-zenhei noto-fonts noto-fonts-cjk noto-fonts-emoji noto-fonts-extra
    
    vim /etc/locale.gen
    en_US.UTF-8 UTF-8
    zh_CN GB2312
    zh_CN.GBK GBK
    zh_CN.UTF-8 UTF-8
    locale-gen
    
    echo 'LANG=zh_CN.UTF-8'  > /etc/locale.conf
    echo 'LANG=zh_CN.UTF-8'  > /etc/default/locale
    vim /etc/environment
    LANG="zh_CN.GB2312" LC_ALL="zh_CN.GBK"
    
    sudo dpkg-reconfigure locales
    reboot
##### Network setting

`networkmanager`

    vim /etc/network/interfaces
    auto eth0
    iface eth0 inet static   #dhcp
          address 192.168.1.101/24
          gateway 192.168.1.1
    
    vim /etc/resolv.conf
    nameserver 223.5.5.5
    nameserver 8.8.4.4
`netplan`

    cd /etc/netplan && vim anyname.yaml
    network:
        version: 2
            ethernets:
                eth0:
                    dhcp4: no #yes
                        addresses: [192.168.1.101/24]
                        gateway4: 192.168.1.1
                    nameservers:
                        addresses: [223.5.5.5, 8.8.4.4]

    sudo netplan apply
SSH Server setting

    vim /etc/ssh/sshd_config
    
    Port 22
    ListenAddress 0.0.0.0
    ListenAddress ::
    
    PermitRootLogin yes
    PubkeyAuthentication yes
    PasswordAuthentication yes
### 2. Ports configuration

`22`Close remote ssh port

    systemctl status sshd.service
    systemctl stop sshd.service
    systemctl disable sshd.service
`25`Close remote postfix port

    systemctl status postfix.service
    systemctl stop postfix.service
    systemctl disable postfix.service
`631`Close the network printer port

    systemctl status cups.service
    systemctl stop cups.service
    systemctl disable cups.service
`5355`Close the local DNS port

    vim /etc/systemd/resolved.conf
    LLMNR=0
    
    systemctl restart systemd-resolved.service
`5353`UDP, close avahi lan printer port
Scan port

    netstat -anp | grep 5353
Shut down service

    systemctl status avahi-deamon.socket
    systemctl stop avahi-deamon.socket
    systemctl disable avahi-deamon.socket
`127.0.0.53/54:53`Close

    vim /etc/systemd/resolved.conf
    DNSStubListener=no
    
    ln -sf /run/systemd/resolve/resolved.conf /etc/resolved.conf
`reboot`the system

