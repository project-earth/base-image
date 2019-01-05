# Quick Guide

## Standard Directory Structure

- `BASE_PATH`
  - `SERVICE_NAME`
    - \__init__.py
    - src
      - ...
    - resources
      - config.yml
      - ...
  - server.py
  - requirements.txt
  - setup.py
  - Dockerfile
  - entrypoint.sh

## Configuration Files

## Dockerfile Template

## Library

## Standard Available Environment Variables

A standard service makes the following environments available. These can be used in the standard way
inside of shell scripts.

- SERVICE_NAME
- BASE_PATH
- LIB_PATH
- SVC_PATH
