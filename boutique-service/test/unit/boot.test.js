import EventEmitter from 'events';
import Sinon from 'sinon';
import Chance from 'chance';
import {expect} from 'chai';
import * as boot from '../../src/boot';

const chance = new Chance();

function buildMockMongoose() {
    return {
        connect: new Sinon.stub(),
        connection: new EventEmitter()
    };
}

describe('Unit Tests > boot', () => {
    describe('connectToMongo', () => {
        it('attempts to connect to the mongo database described and resolves promise', done => {
            const connectionString = chance.string({length: 100});
            const mongoose = buildMockMongoose();

            function assertion(){
                expect(mongoose.connect.calledWith(connectionString)).to.be.ok;
                done();
            }

            boot.connectToMongo(mongoose, connectionString)
                .then(assertion)
                .catch(done);

            mongoose.connection.emit('open');
        });


        it('returns a rejected promise when connection fails', done => {
            const expectedError = new Error('test error');
            const connectionString = chance.string({length: 100});
            const mongoose = buildMockMongoose();

            function assertion(outputError){
                expect(outputError).to.equal(expectedError);
                done();
            }

            boot.connectToMongo(mongoose, connectionString)
                .then(() => {
                    done(new Error('Promise should have been rejected'));
                })
                .catch(assertion);

            mongoose.connection.emit('error', expectedError);

        });
    });
});
