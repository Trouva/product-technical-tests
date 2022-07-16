<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\View;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {

    $http = new \GuzzleHttp\Client();

    $response = $http->get('https://4149o8lffa.execute-api.eu-west-1.amazonaws.com/challenge/boutiques');

    $result = json_decode((string)$response->getBody(), true);

    return View::make('welcome')->with('boutiques', $result);
});
