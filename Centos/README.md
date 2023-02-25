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

    sudo yum install unzip tar gzip htop
    sudo dnf install epel-release
    sudo dnf install neofetch
    sudo dnf install iftop
    sudo yum install openssh-server
