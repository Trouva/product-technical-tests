export default function attachRoutes({ models, router, handlers }) {
    /**
     * @api {get} /v1/boutiques Return a list of all boutiques
     * @apiName BoutiqueList
     * @apiGroup Boutiques
     * @apiVersion 1.0.0
     *
     * @apiDescription Returns the complete list of boutiques
     *
     * @apiSuccessExample {json} Success-Response:
     *     HTTP/1.1 200 OK
     *     {
     *       "location": {
     *         "lon": -0.0757307,
     *         "lat": 51.52338109999999
     *       },
     *       "_id": "5234d2b244e937489c00011c",
     *       "logo": {
     *         "url": "https://res.cloudinary.com/streethub/image/upload/brand/530df3dc6aa953000000014d/nqHF2T7qTjsKq8lE3ugn"
     *       },
     *       "founder_quote": "\"Our mission at Maiden is simple: to make fun, quality gifts accessible to everyone.\"",
     *       "description": "First established in 2009 by Noah Crutchfield, Maiden has become a legendary fixture in Shoreditch's creative independent community. Noah's empire has since expanded to two wonderful shops at Boxpark Shoreditch; THE GIFT BOX & THE PLAY BOX both stocking the different and ever updated bright, eclectic range of gifts that Maiden has become renowned for. A destination for those seeking an original gift, Maiden also plays host to design-led homewares with a humorous twist. ",
     *       "slug": "maiden-in-e16hu",
     *       "name": "MAIDEN"
     *     }
     *
     */
    router.get('/boutiques', handlers.boutiques.bind(undefined, {models}));
}
