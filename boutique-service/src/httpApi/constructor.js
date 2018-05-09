import compression from 'compression';
import _ from 'lodash';
import cors from 'cors';
import * as models from '../models';

export default function buildAPI(express, routes) {
    // Build express app
    const app  = express();

    // let express trust & set x-forwarded-for value to req.ip
    app.enable('trust proxy');

    app.use(compression());
    app.use(cors({
        origin: function(origin, next) {
            const whitelist = [
                'http://localhost:3051'
            ];

            next(null, _.includes(whitelist, origin));
        },
        credentials: true
    }));

    app.use((req, res, next) => {
        res.header('Cache-Control', 'no-cache');
        next();
    });

    // Simple health check URL to confirm the service is up
    app.get('/ping', (req, res) => {
        res.send('pong');
    });

    app.use('/docs/', express.static('../../docs'));

    _.each(routes, config => {
        const router = express();

        config.routes({models, router, handlers: config.handlers});
        router.use(config.error);

        app.use(`/${config.namespace}`, router);
    });

    // General error handler
    app.use((err, req, res, next) => {
        console.error(err.stack);
        res.setStatus(500);
        res.send(err.message);
    });

    return app;
}
