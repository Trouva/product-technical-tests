import mongoose from 'mongoose';

const { Schema } = mongoose;

export default {
    name: Schema.Types.String,
    slug: Schema.Types.String,
    location: {
        lon: Schema.Types.Number,
        lat: Schema.Types.Number
    },
    description: Schema.Types.String
};
