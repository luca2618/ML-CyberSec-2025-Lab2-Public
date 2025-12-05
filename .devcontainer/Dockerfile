#ubuntu base image
FROM ubuntu:latest
# add python 3.8
# Install Python + venv + pip
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-venv \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/radareorg/radare2
RUN cd radare2 && sys/install.sh
# set working directory
WORKDIR /app
# copy requirements file
COPY requirements.txt .
# Create a venv
RUN python3 -m venv /venv

# Make that venv the default Python in the container
ENV PATH="/venv/bin:$PATH"

# Now installs go into /venv, not system Python
RUN pip install --no-cache-dir -r requirements.txt

RUN r2pm -U
RUN r2pm -i r2dec

# Optional: make a non-root user (VS Code likes this)
# RUN useradd -m dev
# USER dev
WORKDIR /workspace