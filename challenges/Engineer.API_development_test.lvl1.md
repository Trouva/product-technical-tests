# Engineering Technical Test: API Development

As an engineer at Trouva one of your responsibilities will be the maintenance and evolution of our APIs.

We have an ever growing number of services mostly written in Javascript (though a few in Python) and a large chunk of core functionality powered by our original "monolith". Many of these services follow a similar design pattern to what you will see in the `boutique-service`, though they fork off to support their individual characteristics. This common structure allows us to quickly deploy into our hosted Docker clusters from the first commit in a project. However it isn't meant to be restrictive, for example there are also a number built with the [Serverless framework](https://serverless.com/) on top of [AWS Lambda](https://aws.amazon.com/lambda/) - the best solution is up to the engineering team working on the problem.

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

`/v1/boutiques/near?latitude=51.5282302&longitude=-0.1045952&limit=5`

And to start with we are going to have the API return the boutique_id and distance in meters:

```
HTTP/1.1 200 OK
[{
  "boutique_id": "5234d2b244e937489c00011c",
  "distance": 370
}]
```

The basic route has been setup already in [routes.js](./boutique-service/src/httpApi/v1/routes.js) and a stub handler for the api request in [boutiquesNear.js](./boutique-service/src/httpApi/v1/handlers/boutiquesNear.js).
