FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y lsb-release && \
  curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc https://download.docker.com/linux/debian/gpg && \
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
    https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list && \
  apt-get update && apt-get install -y docker-ce
RUN usermod -a -G docker jenkins
RUN gpasswd -a jenkins docker

