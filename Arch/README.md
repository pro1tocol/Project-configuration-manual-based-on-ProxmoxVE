building..

### Startup items settings

    BIOS = seaBIOS
    virtIO SCSI
### Initialization settings([archlinux](https://mirrors.ustc.edu.cn/archlinux/images/))

    mkdir workspace && wget https://mirrors.ustc.edu.cn/archlinux/images/v20230301.130409/Arch-Linux-x86_64-basic-20230301.130409.qcow2
    cd workspace/ && mv Arch-Linux-x86_64-basic-20230301.130409.qcow2 archlinux.qcow2
    sudo qm importdisk 100 archlinux.qcow2 SATA250
    sudo qm disk resize 100 scsi0 70G
### BIOS settings

    'e' to edit
    search 'Linux' go to the end, write 'init=/bin/bash'
    ctrl + x
    mount -n -o remount，rw /
    passwd
    reboot
### User settings

    useradd -m -G wheel -s /bin/zsh alarm
    passwd alarm
    EDITOR=vim visudo
    %wheel ALL=(ALL: ALL) ALL
### Language settings

    vim /etc/locale.gen
    en_US.UTF-8 UTF-8
    zh_CN.UTF-8 UTF-8
    locale-gen
    
    echo 'LANG=zh_CN.UTF-8'  > /etc/locale.conf
    echo 'LANG=zh_CN.UTF-8'  > /etc/default/locale
    vim /etc/environment
    LANGUAGE=zh_CN.UTF-8
    LC_ALL=zh_CN.UTF-8
    
    perl -e exit
### Sddm login settings

    vim /usr/lib/sddm/sddm.conf.d/default.conf
    # Comma-separated list of users that should not be listed
    HideUsers=sync
    # Maximum user id for displayed users
    MaximumUid=60000
    # Minimum user id for displayed users
    MinimumUid=0
    
    vim /etc/pam.d/sddm
    #auth    required        pam_succeed_if.so user != root quiet_success
    auth    sufficient      pam_succeed_if.so user ingroup nopasswdlogin
### Freerdp install

point to the client

    pacman -S krdc freerdp
point to the server

    yay -S fuse patch autoconf automake pkg-config meson fakeroot gcc clang make
    yay -S xrdp
    yay -S xorgxrdp
    echo 'allowed_users=anybody' > /etc/X11/Xwrapper.config
    echo '/usr/lib/plasma-dbus-run-session-if-needed startplasma-x11' > ~/.xinitrc
    sudo systemctl enable xrdp.service
    sudo systemctl enable xrdp-sesman.service
    sudo reboot
    
    vim /etc/polkit-1/rules.d/49-nopasswd_global.rules
    polkit.addRule(function(action, subject) {
        if (subject.isInGroup("wheel")) {
            return polkit.Result.YES;
        }
    });
