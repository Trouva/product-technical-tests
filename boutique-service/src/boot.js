import express from 'express';
import Bluebird from 'bluebird';
import mongoose from 'mongoose';
import apiConstructor from './httpApi/constructor';
import v1api from './httpApi/v1';

function connectToMongo(){
    mongoose.connect('mongodb://mongo_database/test');

    return new Bluebird((resolve, reject) => {
        const db = mongoose.connection;
        db.on('error', reject);
        db.once('open', resolve);
    });
}

function initHttpApi(){
    return new Bluebird((resolve, reject) => {
        try {
            const routeConfig = [v1api];
            const api = apiConstructor(express, routeConfig);
            return resolve(api);
        } catch (err) {
            return reject(err);
        }
    })

    return Bluebird.resolve();
}

export default function boot(config){
    return connectToMongo()
        .then(initHttpApi)
        .then(api => {
            return {api};
        });
}
