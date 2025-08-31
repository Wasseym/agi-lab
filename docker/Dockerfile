FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3 python3-venv python3-pip git && rm -rf /var/lib/apt/lists/*
WORKDIR /workspace/agi-lab
COPY . .
RUN pip3 install --upgrade pip && pip3 install -e .
CMD ["/bin/bash"]
