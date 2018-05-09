export default function boutiques({models}, req, res, next) {
    const Boutique = models.boutique;
    Boutique.find({})
        .then(boutiques => {
            res.send(boutiques);
        })
        .catch(next);
}
