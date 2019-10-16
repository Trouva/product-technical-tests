# Engineering Technical Test: Front End Development

As an engineer at Trouva one of your responsibilities will be the prototyping of new experiences that we want to bring to our applications.

## Objective

Unlock the ability to discover boutiques based on physical proximity

## The Scenario and Challenge

We are working on a broader project to improve the experience of discovering new independent shops on Trouva, which we call boutiques. Though a lot of the Trouva experience is delivered through Trouva.com, our roots are in the physical high streets and we still want to help our users explore the best boutiques in person. With our ever growing network there is nearly always a Trouva boutique nearby.

Your squad are spending a couple of days prototyping an experience that will let a visitor on trouva.com find the 5 boutiques closest to them. The current idea is to use the browser's [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation) to get the user coordinates and then find the boutiques closest to them. We would like you to handle developing an MVP of an experience that can determine the users location and find the 5 closest boutiques.

Then next week we are going to hand the tool over to our sales team who are out on the ground around the country signing up new boutiques to see how it works.

## Key result

An proof of concept web app that utilises the [GeoLocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) to get the user position and display the 5 nearest boutiques.

## The requirements

You should develop a web app that works in at least the latest version of Chrome that:

1. Connects to the API endpoint to download all of the boutique data (filtering by location on the API will come later)
2. Gets the users coordinates from the browser GeoLocation API
3. Renders onto the screen the 5 boutiques that are closest from the dataset downloaded in (1)

You can use any technologies or frameworks that you want to develop the experience.

Please include a Readme which outlines what you did and why, considerations, how to run it, etc.

## Accessing the data

You have two choices:

### Use local endpoint

This repository comes with a docker-compose setup that will spin up an API with boutique data. You can then access the data from the following endpoint: `http://localhost:3050/v1/boutiques`

More information on the Docker Compose setup can be found in the Readme at the root of this repository.

### Use public endpoint

The data can also be accessed via the following public endpoint: `https://4149o8lffa.execute-api.eu-west-1.amazonaws.com/challenge/boutiques`

## Submitting the challenge

Please clone/fork this repo to your personal computer and create a branch to hold your work, committing to Git as you go. You should put your application into the `web-app` folder.

Once you are ready to submit, we would like you to create a zip file of your branch and send it over to us.

1. To create a Zip archive of your branch use: `git archive -o ./trouva-test.zip <your_branch_name>`
2. Then please make it available in a shared Dropbox/Google Drive, emailing it to `tech-test@trouva.com`
