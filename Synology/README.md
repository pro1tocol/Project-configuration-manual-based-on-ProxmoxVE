# Install the Synology system and other related deployments

### you need dowmload two files

1. dowload the [v1.04b.for.dms.6.2.1.synoboot-ds918](https://github.com/pro1tocol/Project-configuration-manual-based-on-ProxmoxVE/blob/main/Synology/v1.04b.for.dms.6.2.1.synoboot-ds918.zip)
2. search web and get - DSM_DS918+_*.pat -

Upload to the PVE virtualization platform when ready

    midkr Workspace/
    scp 'DSM_DS918+_*.pat' ../Workspace/
    scp 'v1.04b.for.dms.6.2.1.synoboot-ds918.zip' ../Workspace/
Set mirror passthrough

    unzip v1.04b.for.dms.6.2.1.synoboot-ds918.zip
    cd ../Workpace/v1.04b.for.dms.6.2.1.synoboot-ds918/
    # convert image format
    qemu-img convert -f raw -O qcow2 synoboot.img synoboot.qcow2
    # assign mirror mount number (≥100) and hard disk
    qm importdisk 111 synoboot.qcow2 STAT250G
Directly pass free hard drives to Synology

    # show hard drive list
    ls -l /dev/disk/by-id/
    qm set 110 --sata1 /dev/disk/by-id/ata-KINGSTON_RBU-SNS2035q2911GF_628114B99281B638
The boot is set to sata0, not a direct hard disk, but a mirror image !
