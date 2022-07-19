# Engineering Technical Test: API Development

As an engineer at Trouva one of your responsibilities will be the maintenance and evolution of our APIs.

We have an ever growing number of services mostly written in Javascript and a large chunk of core functionality powered by our original "monolith". Many of these services follow a similar design pattern to what you will see in the `boutique-service`, though they fork off to support their individual characteristics. This common structure allows us to quickly deploy into our hosted Docker clusters from the first commit in a project. However it isn't meant to be restrictive, for example there are also a number built with the [Serverless framework](https://serverless.com/) on top of [AWS Lambda](https://aws.amazon.com/lambda/) - the best solution is up to the engineering team working on the problem.

For the purposes of this challenge we have setup a simple service to return a list of boutiques across the UK and the rest of Europe that you can find on Trouva. It is very basic, but should demonstrate some of the tools for accessing and returning data within the `boutique-service`.

## Objective

Unlock the ability to discover boutiques based on physical proximity

## Key result

An endpoint that returns the 5 closest boutiques to a set of coordinates

## The Scenario and Challenge

We are working on a broader project to improve the experience of discovering new independent shops on Trouva, which we call boutiques. Though a lot of the Trouva experience is delivered through Trouva.com, our roots are in the physical high streets and we still want to help our users explore the best boutiques in person. With our ever growing network there is nearly always a Trouva boutique nearby.

Your squad are spending a couple of days prototyping an experience that will let a visitor on trouva.com find the 5 boutiques closest to them. The current idea is to use the browser's [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation) to get the user coordinates and then find the boutiques closest to them. We would like you to handle developing an MVP of an API endpoint that can take these coordinates and return the 5 closest boutiques.

Then next week we are going to hand the tool over to our sales team who are out on the ground around the country signing up new boutiques to see how it works.

## The requirements

We have agreed on an API request structure:

And to start with we are going to have the API return the boutique name and the location in lat,lng:

```
HTTP/1.1 200 OK
[{
  _id: "58f8993879b34604006c2f1b",
  name: "Store Thirty3",
  slug: "store-thirty3-in-ss91sw",
  location: {
    lon: 0.6539279000000001,
    lat: 51.5423065
  },
  description: "Store Thirty3 prides itself on being an ever-changing, inspirational boutique full of beautiful homeware and lifestyle products with a distinctly Scandinavian feel. Their range includes designer homeware from brands like House Doctor and Bloomingville, luxury clothing from brands including Saint Tropez, Soaked In Luxury and Coster Copenhagen, stunning jewellery and a collection of bags and accessories.",
  founder_quote: ""
},
...]
```

## Submitting the challenge

Please clone/fork this repo to your personal computer and create a branch to hold your work, committing to Git as you go.

Once you are ready to submit, we would like you to create a zip file of your branch and email it over to us.

1. To create a Zip archive of your branch use: `git archive -o ./trouva-test.zip <your_branch_name>`
2. Then please email it to technical-test@streethub.com
