import routes from './routes.js';
import * as handlers from './handlers/index.js';
import errorHandler from './error.js';

export default {
    namespace: 'v1',
    routes,
    handlers,
    error: errorHandler
};
