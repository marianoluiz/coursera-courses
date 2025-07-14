# The FROM instruction initializes a new build stage and specifies the base image that subsequent instructions will build upon.
FROM node:9.4.0-alpine
# The COPY command enables us to copy files to our image.
COPY app.js .
COPY package.json .

# The RUN instruction executes commands.
RUN npm install &&\
    apk update &&\
    apk upgrade

# The EXPOSE instruction exposes a particular port with a specified protocol inside a Docker Container.
EXPOSE  8080

# The CMD instruction provides a default for executing a container, or in other words, an executable that should run in your container.
CMD node app.js
