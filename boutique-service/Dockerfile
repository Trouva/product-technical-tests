FROM node:carbon

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN cd /usr/src/app/ && npm install --production

# Bundle app source
COPY ./src/index.js /usr/src/app/index.js
COPY ./dist /usr/src/app
COPY ./docs /usr/src/app/docs

EXPOSE 3050
CMD [ "node", "index.js" ]
