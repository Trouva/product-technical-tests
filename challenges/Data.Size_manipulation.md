# Data Engineer Test: Sizes & Variants

## Background

One of our core responsibilities at Trouva is to provide an easy-to-use inventory management solution to our boutiques. Being able to provide stock information on sizes and other variants is fundamental to keep the stock accuracy high. A couple of years ago we opened up third party integrations (commonly known as feeds) to provide a temporary solution for boutiques that have an existing system in place, until we're able to provide a full in-store POS solution.

Every few hours an automated system runs and syncs the feed with the inventory information we hold. It will create new entities (products, sizes etc) if they don't exist or update the stock levels of the inventory. A direct consequence of the feed sync, is that we extend our universe of sizes with any information that is coming through the feeds. If a feed for example has a size "s" and we only have "small" in our database, the system will generate a new size "s". Given there are no checks at all even "Small", "smAll" and "smaLL" will be different sizes. To add insult to injury, we don't even know if it's a size, it could be a color, a material or something else.

## Objective

Help us sanitise the current data as a first step towards full standardisation

## Potential action plan

1. Analyse the `./mongo-seed/sizes.json`
2. Identify core issues
3. Outline the strategy you would propose to cleanse the data
4. Perform a data cleansing operation

## Key results

1. A document, deck or handwritten napkin outlining the core issues you've identified & the strategy you'd follow to improve
2. A script or program performing the data cleansing operation you'd run first
3. [BONUS] The second most important data cleansing operation you'd run

## Notes
You're totally free to do whatever you want to the `sizes.json` as long as you can describe succinctly how we would be
able to run it ourselves to get to the same result.

## Submitting the challenge

Please clone/fork this repo to your personal computer and create a branch to hold your work, committing to Git as you go.

Once you are ready to submit, we would like you to create a zip file of your branch and email it over to us.

1. To create a Zip archive of your branch use: `git archive -o ./trouva-test.zip <your_branch_name>`
2. Then please email it to george@trouva.com
