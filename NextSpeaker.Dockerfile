# set base image (host OS)
FROM ubuntu:20.04
# FROM python:3.8
# FROM tensorflow/tensorflow:2.4.1

# install required packages
RUN apt-get update && apt-get install --no-install-recommends -y python3.8 python3-pip python3.8-dev ffmpeg

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements-next-speaker.txt .

# install dependencies
RUN pip3 install -r requirements-next-speaker.txt

# copy the content of the local src directory to the working directory
COPY submission/ .

# command to run on container start
CMD [ "python3", "./main_next_speaker.py" ]