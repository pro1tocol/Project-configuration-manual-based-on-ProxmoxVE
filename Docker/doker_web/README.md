# Data structure

    ├── docker-compose.yml
    ├── mysql/
    ├── mysql.env
    ├── nginx/
    |  └── nginx.conf
    ├── php/
    |  └── Dockerfile
    └── typecho/

### step 1 Certificate application

    sudo apt install wget curl vim git zip socat
    curl https://get.acme.sh | sh
    ln -s  /root/.acme.sh/acme.sh /usr/local/bin/acme.sh
    
    acme.sh --set-default-ca --server letsencrypt
    acme.sh --register-account -m your@Email.com
    acme.sh  --issue -d your-web.domain-name.com  --standalone -k ec-256
    
    cd docker_web
    acme.sh --installcert -d your-web.domain-name.com --ecc  --key-file   ./your.key   --fullchain-file ./your.crt
### step 2 Download and create the necessary file directories

    mkdir mysql/
    mkdir typecho/ && cd typecho/
    wget https://github.com/typecho/typecho/releases/download/v1.2.0/typecho.zip
    unzip typecho.zip
    cd ..
### step 3 Use switching technology

    wget -O box.sh https://raw.githubusercontent.com/BlueSkyXN/SKY-BOX/main/box.sh && chmod +x box.sh && clear && ./box.sh
check`18` and SWAP partition expanded to twice the size of memory

### step 4 RUN

    docker-compose up -d
    docker-compose ps
    docker-compose down

    
