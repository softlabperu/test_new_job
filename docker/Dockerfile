# Copyright 2013 Thatcher Peskens
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM debian:9

MAINTAINER Softlabperu

# Install required packages and remove the apt packages cache when done.
RUN apt update && \
    apt upgrade -y && \
    apt install -y \
  	git \
  	nginx \
  	python3 \
  	libpq-dev \
  	supervisor \
  	python3-dev \
  	python3-pip \
  	python3-setuptools && \
  	pip3 install -U pip setuptools && \
    rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY docker/nginx-app.conf /etc/nginx/sites-available/default
COPY docker/nginx-app.conf /etc/nginx/sites-enable/default
COPY docker/supervisor-app.conf /etc/supervisor/conf.d/

COPY requirements.txt /home/docker/code/
RUN pip3 install -r /home/docker/code/requirements.txt

# add (the rest of) our code
COPY . /home/docker/code/

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
WORKDIR /home/docker/code/
#RUN DATABASE_URL=none python3 manage.py collectstatic --noinput
#
EXPOSE 80
CMD ["supervisord", "-n"]
