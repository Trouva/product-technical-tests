import supertest from 'supertest';
import {expect} from 'chai';
import boot from '../../../../src/boot';

describe('Integration tests > httpApi > v1 > boutiques', function(){

    let api;

    before(() => {
        return boot({})
            .then(outputs => {
                api = outputs.api;
            });
    });

    it('should return boutiques', () => {
        return supertest(api)
            .get('/v1/boutiques')
            .expect(200)
            .then(response => {
                expect(response).to.be.ok;
            });
    });
});
