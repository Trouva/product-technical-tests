import Boutique from '../../../models/boutique';

export default function boutiques(req, res, next) {
    Boutique.find({})
        .lean()
        .then(boutiques => {
            res.send(boutiques);
        })
        .catch(next)
}
