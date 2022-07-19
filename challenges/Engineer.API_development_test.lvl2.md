# Engineering Technical Test: API Development

As an Engineer at Trouva one of your responsibilities will be the maintenance and evolution of our APIs.

We have an ever growing number of services mostly written in Javascript and a large chunk of core functionality powered by our original "monolith". Many of these services follow a similar design pattern to what you will see in the `boutique-service`, though they fork off to support their individual characteristics. This common structure allows us to quickly deploy into our hosted Docker clusters from the first commit in a project. However it isn't meant to be restrictive, for example there are also a number built with the [Serverless framework](https://serverless.com/) on top of [AWS Lambda](https://aws.amazon.com/lambda/) - the best solution is up to the Engineering team working on the problem.

For the purposes of this challenge we have setup a simple service to return a list of boutiques across the UK and the rest of Europe that you can find on Trouva. It is very basic, but should demonstrate some of the tools for accessing and returning data within the `boutique-service`.

## Objective

Enrich the boutique information we hold with external data

## Key result

Each boutique should have a Google Places ID (if it exists)

## The Scenario and Challenge

We've received notice, that we've got a new partner who is about to send us a list of 25,000 physical shops in the UK. We need to go through each of them manually, to sort out which shops meet our criteria (quality, brands, location, offline presence etc.).

To help the Discovery Team who'll be handling the manual process, your squad has decided to build an experience that centralises as much information as possible in one interface so that they can take decisions quickly. Given that every second counts, you're starting to build out a new capability in the boutique-service which stores the Google Places ID of the boutique to reduce the calls required on the client.

You've taken on the responsibility to retrieve & store the Google Places ID in the `boutique-service` for new & existing boutiques so that the response to the client is as fast as possible. 

## The requirements

We have agreed to extend the Schema with a new field:

```
google_places_id
```

We know that we need to account for:
1. In some cases the result may be negative, meaning there is no Google Place for a boutique
2. We need this information to be stored both for existing and new boutiques, as well as refreshed when a boutique is updated

Reminder: During the setup of this project, your local db is seeded with a list of existing boutiques

## Important

You do not need to configure a Google API account to fetch the data - you can either Mock the request or Simply fake the call to Google and return a random string.

## Deliverables
You've determined with the squad that you have the following deliverables:
1. Populate all existing boutiques in the database with their Google Places ID 
2. Whenever a new boutique is create or updated, you need to retrieve and store the Google Places ID
3. Return the Google Places ID as part of the API response
4. Please include a Readme which outlines what you did and why, considerations, how to run it, etc.

## Submitting the challenge

Please clone/fork this repo to your personal computer and create a branch to hold your work, committing to Git as you go.

Once you are ready to submit, we would like you to create a zip file of your branch and email it over to us.

1. To create a Zip archive of your branch use: `git archive -o ./trouva-test.zip <your_branch_name>`
2. Then please email it to tech-test@trouva.com.  (Note: you may have to alternatively email us a link to a zip stored in Google Drive/Dropbox)
