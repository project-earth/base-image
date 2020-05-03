
# Quick Guide

The base path can be built using the command `docker build . -t baseimage`. From there, adding `FROM baseimage` as the first line of a service's docker file builds a service according the standardized template described below.


# Standard Directory Structure

Services based on this base image are expected to have a certain directory structure. This is summarized in the following diagram. The `tests` directory should mirror the `src` directory where filenames are given a `_tests.py` suffix.  

```
- `BASE_PATH`
| - `SERVICE_NAME`
| | - __init__.py
| | - src
| | | - ...
| | - resources
| | | - config.yml
| | | - ...
| - tests
| | - ...
| - server.py
| - requirements.txt
| - setup.py
| - Dockerfile
| - entrypoint.sh
```


# Configuration Files


# Dockerfile Template

The provided `Dockerfile.template` file sets the structure for the what the typical service Dockerfile will look like. Typically the only thing you must modify to get a working Dockerfile in from this template is to set the service name and to install dependencies that can't be installed in the `requirements.txt` file.


# Library

In addition to defining a standard directory structure and docker image templates, services built on this base image have access to a basic python library for accessing service level information. For example, you can globally fetch the service configuration in the form of a Python dictionary with a single import statement: `from baseimage.config import CONFIG`.  Under the `baseimage`, there are also modules for creating appropriately configured Python logging objects and Flask servers.


# Standard Available Environment Variables

A standard service makes the following environments available. These can be used in the standard way inside of shell scripts and are also made available in the parsed configuration file by the configuration parser (as a developer, you do not need to explicitly include them in the configuration).

- **`SERVICE_NAME`:** The name of the service. Defined in the Dockerfile by the developer who should take care that it is used to name the main package directory. In the `CONFIG` dictionary, this is available as `CONFIG['service_name']`.

- **`BASE_PATH`:** This directory is derived in the Dockerfile as `$LIB_PATH/$SERVICE_NAME` and is the directory where all the source files of the service will be added to. This is also the default workdir of the docker image.

Two additional environment variables are available in the docker container but not in the configuration file.

- **`LIB_PATH`:** Fixed variable giving the path to the directory storing all the libraries installed from source which are used by the service. This includes The value will typically be `/opt/lib`.

- **`SVC_PATH`:** Fixed variable giving the path to the directory storing the source code of services running in the container. The value will typically be `/opt/svc`.
