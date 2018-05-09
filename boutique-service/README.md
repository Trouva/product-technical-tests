# boutique-service

An API to provide information on Trouva boutiques

## Quick Start

The `boutique-service` can most simply be run via the Docker Compose file at the root of this test repo:

```
cd ..
docker-compose up
```

If you want to run outside of Docker then you will need to configure your own instance of Mongo and preload it with the seed data found in [../mongo-seed/boutiques.json](Mongo Seed Directory). Once this is sorted you can run `MONGO_CONNECTION_STRING=<your_string> npm start`.

## HTTP API

There is a simple HTTP API that returns a list of Trouva boutiques. This is currently a very simple API that will return all of the boutiques within the database without anything like pagination or filtering.

Full API docs can be found in [./docs/index.html](./docs/index.html).

## Architecture

The an HTTP Api built using Express. It connects to a [https://docs.mongodb.com/](Mongo) database using [http://mongoosejs.com/](Mongoose).

The structure of the application is automatically generated from a service template we have used across a number of projects. However certain bits have been stripped out such as integration with our logging services and some of the standard CI/CD integrations in order to make it easier to work with externally.

## Testing

There are some basic tests implemented using [https://mochajs.org](Mocha) as the test runner and [http://www.chaijs.com/](Chai) for assertions. In a real life project we would likely have used [https://github.com/avajs/ava](Ava) for the testing, and that is built into the project template, however the test have been implemented with Mocha/Chai as people are more likely to be immediately familiar with that ecosystem of tools.
