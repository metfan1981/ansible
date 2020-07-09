#!/bin/bash
  
which docker >> /dev/null

if [ $? -ne 0 ]; then
  echo "Docker will be installed"
  apt update -y
  /bin/bash /home/get-docker.sh
  rm $(which docker-compose)
  curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  chmod +x /usr/local/bin/docker-compose
else
  echo "Docker is installed already"
fi
