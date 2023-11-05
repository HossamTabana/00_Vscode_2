FROM ubuntu:latest
WORKDIR /code
RUN apt-get update && apt-get -y upgrade
RUN pip install pip --upgrade
ADD requirements.txt /code
RUN pip install -r requirements.txt
RUN mkdir /notebooks
CMD jupyter notebook --no-browser --ip 0.0.0.0 --port 8888 /notebooks