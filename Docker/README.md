# This docfile use to build something
-------------------------------------

### PVE environment adjustment content

1.Uncheck "Unprivileged Containers"

2.After the creation is complete, you need to check "nesting" under "Options-Function"

    cd /etc/pve/lxc/xxx.conf
    lxc.apparmor.profile: unconfined
    lxc.cgroup.devices.allow: a
    lxc.cap.drop:
-------------------------------------
### Apt repository installation
Install basic environment

    sudo apt update
    sudo apt install ca-certificates curl gnupg lsb-release
Install key

    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
Install sources

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
Build tools

    sudo apt update
    sudo apt install docker-ce docker-ce-cli containerd.io docker-compose
-------------------------------------
## Third party container

[NginxProxyManager/ChatgptWeb](https://allencj.com/archives/1536)

[chenzhaoyu94/chatgpt-web](https://hub.docker.com/r/chenzhaoyu94/chatgpt-web)

-------------------------------------
### Local container settings

Docker

    --security-opt apparmor=unconfined
Docker-compose

    services:
      security_opt:
        - apparmor=unconfined


    
