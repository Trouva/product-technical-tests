import express from 'express';
import Bluebird from 'bluebird';
import mongoose from 'mongoose';
import apiConstructor from './httpApi/constructor';
import v1api from './httpApi/v1';

export function connectToMongo(mongoose, dbConnectionString){
    mongoose.connect(dbConnectionString);

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
    });
}

export default function boot({mongoConnectionString}){
    return connectToMongo(mongoose, mongoConnectionString)
        .then(initHttpApi)
        .then(api => {
            return {api};
        });
}
