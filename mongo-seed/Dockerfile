FROM mongo:3.6.4

COPY boutiques.json /boutiques.json
CMD mongoimport --host mongo_database --db project --collection boutiques --type json --file /boutiques.json --jsonArray
