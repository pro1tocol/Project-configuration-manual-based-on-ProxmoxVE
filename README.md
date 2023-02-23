# Project-configuration-manual-based-on-ProxmoxVE
### This project is used to record related operations of the PVE virtualization platform and related settings of virtual machine deployment
-------------------------------------------------

## About PVE, click: [https://pve.proxmox.com/wiki/Main_Page](https://pve.proxmox.com/wiki/Main_Page)
## You can choose the [Etcher](https://www.balena.io/etcher) tool for image burning

The process of system installation and use will not be repeated

#### 1. Update source code related configuration

    vim /etc/apt/sources.list
    # Switch to Chinese sources
    deb http://mirrors.ustc.edu.cn/debian bullseye main contrib non-free
    deb http://mirrors.ustc.edu.cn/debian bullseye-updates main contrib non-free
    deb http://mirrors.ustc.edu.cn/debian bullseye-proposed-updates main contrib non-free
    deb http://mirrors.ustc.edu.cn/debian-security/ bullseye-security main contrib non-free
update to the unofficial Proxmox VE (not recommended for production)

    vim /etc/apt/sources.list.d/pve-enterprise.list
    # Switch to Chinese sources
    deb [trusted=yes] http://download.proxmox.com/debian bullseye pve-no-subscription
    deb [trusted=yes] https://mirrors.ustc.edu.cn/proxmox/debian/pve bullseye pve-no-subscription
    
#### 2. Start PVE host hardware/network card/graphics card transparent transmission
Default startup item settings

    vim /etc/default/grub
    # hardware passthrough optional 'amd_iommu=on' or 'intel_iommu=on'
    # 
    GRUB_DEFAULT=0
    GRUB_TIMEOUT=5
    GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
    GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on iommu=pt video=efifb:off"
    GRUB_CMDLINE_LINUX=""
    
    update-grub
Enable modules

    vim /etc/modules
    # enable virtualization platform passthrough hardware modules
    vfio
    vfio_iommu_typel
    vfio_pci
    vfio_virqfd
    
    reboot
`Graphics`card pass-through configuration

    lspci | grep VGA
    # find the corresponding hardware serial number
    lspci -n -s 03:00
    # write the corresponding file according to the result
    echo "options vfio-pci ids=10de:1244" > /etc/modprobe.d/vfio.conf
    echo "options vfio-pci ids=10de:0bee" >> /etc/modprobe.d/vfio.conf
Shield related hardware drivers

    echo "blacklist nvidiafb" >> /etc/modprobe.d/pve-blacklist.conf
    echo "blacklist snd_hda_intel" >> /etc/modprobe.d/pve-blacklist.conf
    echo "blacklist snd_hda_codec_hdmi" >> /etc/modprobe.d/pve-blacklist.conf
    echo "blacklist i915" >> /etc/modprobe.d/pve-blacklist.conf
Update kernel

    update-initramfs -u
