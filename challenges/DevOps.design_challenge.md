# DevOps Challenge: Ecosystem Design

One of the key tasks we want you to help with on joining is working out how to make our development experience faster, easier and more enjoyable for everyone involved.

We are going to provide you with some context into our current configuration for supporting our developers in starting out with an idea locally, work collaboratively together to solve the problem and eventually getting things out into production. But it is not perfect. We are interested to hear your thoughts on how we could go about making it better.

## The Context

At Trouva we started with a single backend service and a few front-end apps, that connected to that API for all their authentication and data processing. After a couple of years running this all locally for development we put that backend service into Vagrant to give a more consistent development experience as the team grew.

Then we started to introduce new backend services and more complicated hybrid front-end apps with server side rendering. To support this we moved to using Docker container both for local development and for deploying into our staging and production environments.

We now have around 10 services running in [Docker](https://www.docker.com/). Locally these are connected together using [Docker Compose](https://docs.docker.com/compose/). Then are deployed into [AWS Elastic Container Service](https://aws.amazon.com/ecs/) in a staging and a production environment, having first been built in our CI process and then deployed using [Terraform](https://www.terraform.io/).

In production things are working ok for now, though we are always looking for ways to improve. However during earlier stages of the development lifecycle we are running into problems.

Running the full ecosystem of services is getting harder, more resource intensive and takes time to ensure all versions of apps are up to date. Which means people are more and more often using our staging environment to test out ideas more and share them with the rest of the team. So the staging environment is becoming less of a pre-deployment last check and more a place to do manual integration tests.

## The Question

The key thing we are interested in is what are your thoughts on a good setup with an ecosystem with multiple services, powered by Docker, to enable effective development and collaboration across the team.

The obvious problems seem to be:

- How can people work locally, but deal with having multiple other services they made be dependent on
- How can we provide a hosted environment to test out ideas and share them with the team. Without completely blowing the budget.

But maybe we are looking at the problem in the wrong way, so feel free to challenge those assumption.

## The Deliverable

We would like you to communicate back to us your ideas on how to approach solving that problem in some form of document you can easily share with us.

Perhaps there are a few things that jump out at you straight away that seem obvious, if you feel you know the complete solution already then just tell us. However you don’t necessarily have all the information on our systems and our way of working - so equally it would be useful to communicate what you see as the big questions and forks of different approaches.

We want to see:
- Your ideas and insight from past experience
- The skeleton of a plan for approaching the project if you had weeks or months to tackle it
- And how you present those ideas back to us


## Submitting the challenge

Once you have something ready email it over to alex@trouva.com. If you have any questions or want some extra insight then also drop George an email and he will be happy to help.
