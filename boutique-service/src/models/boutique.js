import mongoose from 'mongoose';
import boutiqueSchema from '../schemas/boutique.js';

export default mongoose.model('Boutiques', boutiqueSchema);
