import { BoutiquesContext } from '../contexts/BoutiquesProvider'
import { useContext } from 'react'

export const useBoutiques = () => useContext(BoutiquesContext)
