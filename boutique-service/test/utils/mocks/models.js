import mongooseMock from 'mongoose-mock';
import boutiqueSchema from '../../../src/schemas/boutique';

export default function(){
    const boutique = mongooseMock.model('Boutiques', mongooseMock.Schema(boutiqueSchema));

    return {boutique};
}
