This repository hosts the docker base image for containerized micro-service based applications of a small/medium scale (ie. O(20) micro-services running on O(5) machines sharing a single EFS-like filesystem). The base image defines the directory structure that applications can expect in the container including volume-mounted directories and provides tools to access core service functionality (logging, monitoring, configuration). Our base image is built on the [`python3.6-slim` ](https://github.com/docker-library/python/blob/35566cb6b14961c369e935b85b4c8879e6901ccc/3.6/buster/slim/Dockerfile) Docker image.

# Quick Guide

Your application repository should have a directory structure as described in the section [below](#standard-directory-structure). Your application Dockerfile should be based on the template we've [provided]([https://github.com/project-earth/baseimage/blob/master/Dockerfile.template](https://github.com/project-earth/baseimage/blob/master/Dockerfile.template)) in this base image. Furthermore, to fully take advantage of the features provided by the base image, you should use the provided [libraries](#library) for monitoring, logging, and configuration parsing.

It is worth noting that the directory structure of the container revolves around three primary directories:
* **`/opt/lib`:** The path to the directory storing all the libraries installed from source which are used by the service. This library is intended to store clone git repositories of dependencies and other downloaded dependencies. Note that the image does not enforce installation of dependencies from this directory. You can reference the documentation on [dependencies](#dependencies) to see common patterns for accomplishing this.
* **`/opt/svc`:** The directory storing all the libraries installed from source which are used by the service. When the service image is built, the contents of the service repository are copied here.
* **`/opt/dat`:** The path to the directory intended to hold the persistent data of service. Note that at build time, this directory is *not* actually persistent. This directory should be bind or volume mounted during when the container is run. We have a [section](#persistent-storage) of documentation discussing options for accomplishing this.

**Building your service image**
Before building your application image, you need to build the base image using `docker build . -t baseimage`. Then from your service image can be built from the root directory of your service's repository.

**Running your service**
If you are familiar orchestrating, these flags may not apply but we typically run our images detached `-d`, on the host network interfact `--net=host`, and with a bind-mount to a host directory `-v host_data_dir:/opt/dat`.

# Standard Directory Structure

Your application repository should be structure in the following way:

```
- $BASE_PATH
| - $SERVICE_NAME
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

* The `test` directory here is typically expected to mimic the `src` directory but with `test_*` prefixes included for each of the directories and files.
* `requirements.txt` should include the Python requirements for the service. Non-Python requirements should be installed as commands in the Dockerfile.
* `Dockerfile` is the standard Docker build instruction set and should be based on the template Dockerfile found in this repository.
* `entrypoint.sh` is the shell script that should be run to start the service.
* Note that the directory structure here reflects a Python (flask) micro-service that we have typically used this base image with though  does not strictly need to be the case.

# Configuration Files

# Dockerfile Template

# Dependencies

# Library
## Logging
## Configuration
## Monitoring

# Persistent Storage

# Standard Available Environment Variables

A standard service makes the following environments available. These can be used in the standard way
inside of shell scripts and are also made available in the parsed configuration file by the configuration parser (as a developer, you do not need to explicitly include them in the configuration).

- **`SERVICE_NAME`:** The name of the service. Defined in the Dockerfile by the developer who should take care that it is used to name the main package directory. In the `CONFIG` dictionary, this is available as `CONFIG['service_name']`.
- **`BASE_PATH`:** This directory is derived in the Dockerfile as `$LIB_PATH/$SERVICE_NAME` and is the directory where all the source files of the service will be added to. This is also the default workdir of the docker image.
- **`HOST_NAME`:** A variable set on service runtime indicating the running container's ID.
* **`LIB_PATH`:** Fixed variable giving the path to the directory storing all the libraries installed from source which are used by the service. This has a fixed value of `/opt/lib`.
* **`SVC_PATH`:** Fixed variable giving the path to the directory storing the source code of services running in the container. This has a fixed value of `/opt/svc`.
* **`DAT_PATH`:** Fixed variable giving the path to the directory intended to hold the persistent data of service. This has a fixed value of `/opt/dat`.
* **`LOG_PATH`:** Fixed variable giving the path to the directory intended to hold the logs of this service's runtime. This has a fixed value of `/opt/dat/logs/$HOSTNAME`.
