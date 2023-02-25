# test

#### Switch source

    sudo sed -e 's|^mirrorlist=|#mirrorlist=|g' \
         -e 's|^#baseurl=http://mirror.centos.org/$contentdir|baseurl=https://mirrors.ustc.edu.cn/centos|g' \
         -i.bak \
         /etc/yum.repos.d/CentOS-Stream-AppStream.repo \
         /etc/yum.repos.d/CentOS-Stream-BaseOS.repo \
         /etc/yum.repos.d/CentOS-Stream-Extras.repo \
         /etc/yum.repos.d/CentOS-Stream-PowerTools.repo
Clean cache data

    dnf clean all
    dnf makecache
Install daily tools

    sudo yum install unzip tar gzip htop    #prerequisites for installing vscode-server
    sudo dnf install epel-release
    sudo dnf install neofetch
    sudo dnf install iftop
    sudo yum install openssh-server
Switch SHELL

    sudo dnf install util-linux-user        #fix 'chsh' command not found
    chsh -s /bin/zsh
Switch language

    sudo dnf install glibc-langpack-zh.x86_64
    sudo yum -y install langpacks-zh_CN
    
    locale -a
    vim /etc/locale.conf
    . /etc/locale.conf
    locale
