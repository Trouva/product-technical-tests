import { render, screen } from "@testing-library/react";
import BoutiqueDetail from ".";
import { boutiques } from "../../mock/boutiques";

const [boutique] = boutiques;

test("renders BoutiqueDetail", () => {
  render(
    <BoutiqueDetail {...boutique} />
  );

  const name = screen.getByRole('heading', { name: new RegExp(boutique.name, "i") });
  const description = screen.getByText(new RegExp(boutique.description, "i"));

  expect(name).toBeInTheDocument();
  expect(description).toBeInTheDocument();
});
