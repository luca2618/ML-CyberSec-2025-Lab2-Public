#ubuntu base image
FROM ubuntu:latest
# add python 3.8
RUN apt-get update && apt-get install -y python3.8 python3-pip
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/radareorg/radare2
RUN cd radare2 && sys/install.sh
# set working directory
WORKDIR /app
# copy requirements file
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN r2pm -U
RUN r2pm -i r2dec

# Optional: make a non-root user (VS Code likes this)
RUN useradd -m dev
USER dev
WORKDIR /workspace