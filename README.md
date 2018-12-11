# Quick Guide

## Standard Directory Structure

- `BASE_PATH`
  - `SERVICE_NAME`
    - \__init__.py
    - src
      - ...
    - resourc1es
      - ...
  - server.py
  - requirements.txt
  - setup.py
  - Dockerfile
  - entrypoint.sh

## Configuration Files

## The DockerFile Template

1. Set SERVICE_NAME in DockerFile
2. In service entrypoint, call /opt/lib/baseimage/runtime.setup.sh to set the rest of the environment

## Standard Available Environment Variables

A standard service makes the following environments available. These can be used in the standard way
inside of shell scripts.

- SERVICE_NAME
- BASE_PATH
- LIB_PATH
- SVC_PATH
