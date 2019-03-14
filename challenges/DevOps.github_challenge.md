# Devops Challenge

## Part I - Github API

Using the Github API you should be able to query a user’s publicly available github gists.
Implement an application that periodically checks for a user's publicly available gists, this application should also have a web endpoint where it should show the gists for that user that were added since the last visit.

### Expectations

- You can use any programming language you want
- No need to get crazy with HTML/CSS or JSON apis, a simple text response will suffice
- This problem description is intentionally vague, document your assumptions and justify your decisions

### Bonus points

- Good output, clear logging and let us know what its doing
- README file with clear instructions on how to run the application on our local computers

## Part II - The cloud

Let's get that application that you've done onto the cloud.
Periodic checks should run every 3 hours.

### Expectations

- You can use any provisioning tool you want
- You can use any cloud provider you'd like
- You should be able to complete this challenge with the free tier of any major cloud provider and you'll have to show us the deployed application on the web

### Bonus points

- Resiliency 
- Scalability

## Submitting the challenge

Please clone/fork this repo to your personal computer and create a branch to hold your work, committing to Git as you go. You're very welcome to either use 
the existing configuration or implement your own boilerplate. 

Once you are ready to submit, we would like you to create a zip file of your branch and email it over to us.

1. To create a Zip archive of your branch use: `git archive -o ./trouva-test.zip <your_branch_name>`
2. Then please email it to pedro@trouva.com
