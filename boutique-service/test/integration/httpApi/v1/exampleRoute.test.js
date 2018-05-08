import test from 'ava';
import supertest from 'supertest-as-promised';
import boot from '../../../../src/boot';

let api;

test.before(() => {
    return boot({logging: {}})
    .then(outputs => {
        api = outputs.api;
    });
});

test('test', t => {
    t.plan(1);

    return supertest(api)
    .get('/v1/test')
    .expect(200)
    .then(response => {
        t.deepEqual(response.text, 'working: this is a response');
    });
});
