# boutique-service

An API to provide information on Trouva boutiques

## Quick Start

The `boutique-service` can most simply be run via the Docker Compose file at the root of this test repo:

```
cd ..
docker-compose up
```

If you want to run outside of Docker then you will need to configure your own instance of Mongo and preload it with the seed data found in (../mongo-seed/boutiques.json)[Mongo Seed Directory]. Once this is sorted you can run `MONGO_CONNECTION_STRING=<your_string> npm start`.

## HTTP API

There is a simple HTTP API that returns a list of Trouva boutiques. This is currently a very simple API that will return all of the boutiques within the database without anything like pagination or filtering.

The OpenAPI for the boutique can be found here: https://github.com/Trouva/product-technical-tests/blob/master/boutique-service/src/httpApi/v1/routes.js#L28

## Architecture

The an HTTP Api built using Express. It connects to a (https://docs.mongodb.com/)[Mongo] database using (http://mongoosejs.com/)[Mongoose].

The structure of the application is automatically generated from a service template we have used across a number of projects. However certain bits have been stripped out such as integration with our logging services and some of the standard CI/CD integrations in order to make it easier to work with externally.

## Testing

Currently the project contains only unit tests. To run the tests:

> npm run test
