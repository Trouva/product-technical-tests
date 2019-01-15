# Data Engineer Test: Sizes & Variants

## Background

One of our core responsibilities at Trouva is to provide an easy-to-use inventory management solution to our boutiques. Being able to provide stock information on sizes and other variants is fundamental to keep the stock accuracy high. A couple of years ago we opened up third party integrations (commonly known as feeds) to provide a temporary solution for boutiques that have an existing system in place, until we're able to provide a full in-store POS solution.

Every few hours an automated system runs and syncs the feed with the inventory information we hold. It will create new entities (products, sizes etc) if they don't exist or update the stock levels of the inventory. A direct consequence of the feed sync, is that we extend our universe of sizes with any information that is coming through the feeds. If a feed for example has a size "s" and we only have "small" in our database, the system will generate a new size "s". Given there are no checks at all even "Small", "smAll" and "smaLL" will be different sizes. To add insult to injury, we don't have control over what boutique owners put in this field. So we do not even know if it's a size, it could be a color, a material or something else.

## Objective

Help us sanitise the current data as a first step towards full standardisation

## Current challenges

As you can see in `./mongo-seed/sizes.json` the current process has introduced a wide-ranging set of issues
for example ambiguity (is it a size, a material, a colour?) and duplication ("s", "small", "SMALL"). This results
in challenges across the business:

- Our size filters on Trouva.com many times don't make much sense which degrades the customer experience
- It's quite hard for us to streamline communication with the boutiques for example to promote re-stocking behaviour
- On the business intelligence side, it's hard to provide the merchandising team with insights on what sizes sell well
- We aren't able to distinguish between sizes, materials, colours etc. which reduces our capabilities on the consumer side

We won't be able to solve all of this in one go, but as a data engineer you'll be looped in to help figure out how
we can in small incremental steps standardise our size universe and streamline our process.

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

- We assume that you're going to use Python for your technical solution, however it's up to you to choose the right tool for the job
- You don't need to wrap you solution into our docker-compose structure (unless you want to)
- Keep your code in the `./size-sanitizer` folder, you can copy the `mongo-seed/sizes.json` over if you'd like

## Submitting the challenge

Please clone/fork this repo to your personal computer and create a branch to hold your work, committing to Git as you go.

Once you are ready to submit, we would like you to create a zip file of your branch and email it over to us.

1. To create a Zip archive of your branch use: `git archive -o ./trouva-test.zip <your_branch_name>`
2. Then please email it to emma.karydi@trouva.com
