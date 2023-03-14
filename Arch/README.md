building..

### Startup items settings

    BIOS = OVMF
    Add bios startup items to efi's file
    Adjust the position of the startup item
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
