echo "Transpiling code from ES6 with Babel"
rm -r -f dist
./node_modules/.bin/babel src --out-dir dist

echo "Building docker image"
docker build -t trouva-product-test/boutique-service:${version_tag} .

echo "Cleaning up temporary files"
rm -r -f ./dist
