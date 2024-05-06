FROM --platform=linux/amd64 mcr.microsoft.com/devcontainers/python:3.11

ENV PYTHONUNBUFFERED 1

# COPY python_sam_template/layer/requirements.txt /tmp
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt \
#    && rm -rf /tmp/requirements.txt
COPY mastering_bitcoin/requirements.txt /tmp
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt \
   && rm -rf /tmp/requirements.txt
# COPY tests/requirements.txt /tmp
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt \
#    && rm -rf /tmp/requirements.txt
# RUN pip install alembic

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>


