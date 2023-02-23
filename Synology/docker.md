# This article mainly records the relevant deployment of [docker](https://www.docker.com/) applications in the Synology environment

#### Installation can be done in the app store

## Install [jellyfin](https://jellyfin.org/)

    sudo docker pull jellyfin/jellyfin
    
    # configure hard disk and media library without booting
    docker/jellyfin	/config
    /Movie		/media/TV
