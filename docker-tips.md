## How to run tests inside docker

Once you have spun up docker compose with docker-compose up. You can then open an interactive session to work within the `boutique-service` container, with `docker-compose exec boutique-service bash`.

From here you can simply run `npm test` and interact with the service as if it was on your local machine.

## How to install new dependencies via NPM

There are a couple of options, but it is probably cleanest to run the `npm install` from inside the `boutique-service` docker container.

Once you have spun up docker compose with docker-compose up. You can then open an interactive session to work within the `boutique-service` container, with `docker-compose exec boutique-service bash`.

From here you can simply run `npm install` and interact with the service as if it was on your local machine.
