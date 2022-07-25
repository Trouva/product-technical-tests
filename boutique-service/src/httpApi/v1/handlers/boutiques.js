export default function boutiques({models}, _, res, next) {
    const Boutique = models.boutique;
    
    Boutique.find({})
        .then(boutiques => res.send({ boutiques }))
        .catch(next);
}
