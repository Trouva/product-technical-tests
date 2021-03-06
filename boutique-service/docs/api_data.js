define({ "api": [
  {
    "type": "get",
    "url": "/v1/boutiques",
    "title": "Return a list of all boutiques",
    "name": "BoutiqueList",
    "group": "Boutiques",
    "version": "1.0.0",
    "description": "<p>Returns the complete list of boutiques</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"location\": {\n    \"lon\": -0.0757307,\n    \"lat\": 51.52338109999999\n  },\n  \"_id\": \"5234d2b244e937489c00011c\",\n  \"logo\": {\n    \"url\": \"https://res.cloudinary.com/streethub/image/upload/brand/530df3dc6aa953000000014d/nqHF2T7qTjsKq8lE3ugn\"\n  },\n  \"founder_quote\": \"\\\"Our mission at Maiden is simple: to make fun, quality gifts accessible to everyone.\\\"\",\n  \"description\": \"First established in 2009 by Noah Crutchfield, Maiden has become a legendary fixture in Shoreditch's creative independent community. Noah's empire has since expanded to two wonderful shops at Boxpark Shoreditch; THE GIFT BOX & THE PLAY BOX both stocking the different and ever updated bright, eclectic range of gifts that Maiden has become renowned for. A destination for those seeking an original gift, Maiden also plays host to design-led homewares with a humorous twist. \",\n  \"slug\": \"maiden-in-e16hu\",\n  \"name\": \"MAIDEN\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "src/httpApi/v1/routes.js",
    "groupTitle": "Boutiques"
  }
] });
