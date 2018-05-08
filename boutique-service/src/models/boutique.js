import mongoose from 'mongoose';
import boutiqueSchema from '../schemas/boutique'

export default mongoose.model('Boutiques', boutiqueSchema);
