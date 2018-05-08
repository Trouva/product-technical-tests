export default function attachRoutes({ router, handlers }) {
    /**
     * @api {post} /v1/test This is a test route.
     * @apiName Test
     * @apiGroup Test
     * @apiVersion 1.0.0
     *
     * @apiDescription This is a test.
     *
     * @apiParam (Request Body) {String} test1 Test 1.
     * @apiParam (Request Body) {Boolean} test2 Test 2.
     *
     * @apiSuccess (200) {Object} test
     *
     * @apiError (Error 401) NotAuthenticated Test error.
     * @apiError (Error 403) NotAuthorized Test error.
     */
    router.get('/boutiques', handlers.boutiques);
}
