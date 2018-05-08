import test from 'ava';
import handlers from '../../../../../src/httpApi/v1/handlers';

const req = {};
const res = {};

const send = (t, response) => {
    t.deepEqual(response, 'working: this is a response');
};

test('Test handler', t => {
    t.plan(1);

    res.send = send.bind(this, t);

    handlers.test(req, res);
});
