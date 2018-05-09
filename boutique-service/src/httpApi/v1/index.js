import routes from './routes';
import * as handlers from './handlers';
import errorHandler from './error';

export default {
    namespace: 'v1',
    routes,
    handlers,
    error: errorHandler
};
