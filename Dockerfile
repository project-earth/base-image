# ===== Header ===== #
FROM python:3.6-slim

# ===== Setup Environment ===== #
ENV LIB_PATH /opt/lib
ENV SVC_PATH /opt/svc
ENV DAT_PATH /opt/dat
RUN mkdir $LIB_PATH
RUN mkdir $SVC_PATH
RUN mkdir $DAT_PATH
RUN mkdir $DAT_PATH/logs

# ===== Add Source to Environment, Install Library ===== #
ADD . $LIB_PATH/baseimage
RUN pip install -r $LIB_PATH/baseimage/requirements.txt
RUN pip install $LIB_PATH/baseimage
