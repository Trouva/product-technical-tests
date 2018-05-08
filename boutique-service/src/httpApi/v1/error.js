export default function errorHandler(err, req, res, next) {
    if (err.httpResponseCode) {
        res.status(err.httpResponseCode).json({
            status: err.httpResponseCode,
            message: err.message
        });
    } else {
        res.status(500).send();
    }

    const errorBody = {err: err, req: req};

    if (err.name === 'RequestError'){
        errorBody.requestOptions = err.options;
    }

    if (!err.httpResponseCode || err.httpResponseCode === 500) {
        console.error(errorBody);
    } else {
        console.info(errorBody);
    }
}
