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
    zh_CN.UTF-8 UTF-8
    locale-gen
    
    echo 'LANG=en_US.UTF-8'  > /etc/locale.conf
SSH Server setting

    vim /etc/ssh/sshd_config
    
    Port 22
    ListenAddress 0.0.0.0
    ListenAddress ::
    
    PermitRootLogin yes
    PubkeyAuthentication yes
    PasswordAuthentication yes
Network setting

    vim /etc/network/interfaces
    auto eth0
    iface eth0 inet static   #dhcp
          address 192.168.1.101/24
          gateway 192.168.1.1
    
    vim /etc/resolv.conf
    nameserver 223.5.5.5
    nameserver 8.8.4.4
