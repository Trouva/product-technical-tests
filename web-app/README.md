## How to start
composer install
npm install
php artisan serve

## Create a secured localhost
Geolocation API requires a secure connection
brew install ngrok/ngrok/ngrok
ngrok config add-authtoken TOKEN
ngrok http -bind-tls=true site.dev:80
ngrok http 8000

Connect to the gateway

## Run tests
php artisan test

## Structure
I used Laravel, JS and CSS
- Routes -> web-app/routes/web.php -> Access to the API and return the boutiques;
  - Views -> resources/views/welcome.blade.php 
    1 -> Added a google map for orientation;
    2 -> Get the coordinates from navigator geolocation, and add to center of the map, add marker;
    3 -> Get array of locations and get the coordinates;
    4 -> Filter the 5 closer and add markers to them;
- Styles -> web-app/resources/css/app.css -> Map styles
- 
