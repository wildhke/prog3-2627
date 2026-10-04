FROM python:3.12-bookworm

ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        git \
        build-essential \
        make \
        libgl1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /workspaces/project_2026
