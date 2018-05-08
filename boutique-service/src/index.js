import boot from './boot';

boot({
    environment: process.env.NODE_ENV || 'development'
}).then(outputs => {
    const port = process.env.PORT || 3050;
    outputs.api.listen(port);
    console.info(`Listening on port ${port}`);
});
