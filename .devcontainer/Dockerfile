#ubuntu base image
FROM ubuntu:latest
# add python 3.8
RUN apt-get update && apt-get install -y python3.8 python3-pip
RUN apt-get update && apt-get install -y git
# set working directory
WORKDIR /app
# copy requirements file
COPY requirements.txt .

# Optional: make a non-root user (VS Code likes this)
RUN useradd -m dev
USER dev
WORKDIR /workspace