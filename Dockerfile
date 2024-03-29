FROM python:3.6-slim

#ENV PYTHONUNBUFFERED 1
#
#RUN mkdir /code
#WORKDIR /code
#COPY . /code/
#RUN pip install -r requirements.txt

EXPOSE 8080

ARG workspace="none"

RUN apt-get update \
    && apt-get install --assume-yes wget bash-completion unzip


RUN wget https://codejudge-starter-repo-artifacts.s3.ap-south-1.amazonaws.com/backend-project/database/db-setup.sh
RUN chmod 775 ./db-setup.sh
RUN sh db-setup.sh


# Install Workspace for Python

RUN if [ $workspace = "theia" ] ; then \
	wget https://codejudge-starter-repo-artifacts.s3.ap-south-1.amazonaws.com/theia/pre-build.sh \
    && chmod 775 ./pre-build.sh && sh pre-build.sh ; fi

WORKDIR /var/


RUN if [ $workspace = "theia" ] ; then \
	wget https://codejudge-starter-repo-artifacts.s3.ap-south-1.amazonaws.com/theia/build.sh \
    && chmod 775 ./build.sh && sh build.sh ; fi

# Get RUN Script

WORKDIR /var/theia/

RUN if [ $workspace = "theia" ] ; then \
	wget https://codejudge-starter-repo-artifacts.s3.ap-south-1.amazonaws.com/theia/run.sh \
    && chmod 775 ./run.sh ; fi


# End Install for Workspace

RUN mkdir -p /var/app

WORKDIR /var/app

ADD requirements.txt /var/app

# Build the app
RUN wget https://codejudge-starter-repo-artifacts.s3.ap-south-1.amazonaws.com/backend-project/python/build.sh
RUN chmod 775 ./build.sh
RUN sh build.sh

ADD . .

# Run the app
#RUN wget https://codejudge-starter-repo-artifacts.s3.ap-south-1.amazonaws.com/backend-project/python/django/run-2.sh
#RUN ./util/setup.sh
RUN chmod 775 ./util/setup.sh
CMD sh ./util/setup.sh