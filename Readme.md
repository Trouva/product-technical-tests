# Trouva Product Technical Tests

## Challenges

In your briefing you will have been given a link to a specific challenge, though so far there is only one so that keeps it easy.

### Product Engineer

- [Create a nearby boutiques endpoint](./challenges/Engineer.API_development_test.lvl1)

## Pre-requisite Setup

Within this repo you should have everything you need to complete the challenge. There are some skeleton services setup, with example code to get you started and databases pre-filled with data.

The only assumption is that you have some familiarity with Docker, as the different parts are split into docker containers that work together through Docker Compose.

### Installing Docker Compose

The official installation instructions should be all that you need:

https://docs.docker.com/compose/install/

### Spinning up the project

Once Docker Compose is installed, you can run the project through `docker-compose up` from the root of the repo. This may take some time on first boot as it will be pulling down all the dependencies to run each project, but will then get faster on the second iteration.

Once it is all built you can visit `http://localhost:3050/ping` in your browser to check the server is running. And then visit `http://localhost:3050/v1/boutiques` to ensure that the project is communicating with the database correctly.

### If you get stuck with docker?

We can't answer every problem. If you feel really uncomfortable diving into Docker, then don't worry we can teach you later. It is possible to run all of the parts outside of Docker, have a poke around and if you get stuck just drop us an email.

But if you are just stuck on a small things, we have put together some [Docker Tips](./docker-tips.md).
