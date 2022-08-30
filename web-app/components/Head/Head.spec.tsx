import { render, screen } from '@testing-library/react';
import Head from '../Head';

test('renders Trouva Boutiques', () => {
  render(<Head />);
  const linkElement = screen.getByText(/Trouva Boutiques/i);
  expect(linkElement).toBeInTheDocument();
});
