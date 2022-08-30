import { render, screen } from "@testing-library/react";
import TopBar from "./";

const value = "Header value";

test("renders Trouva Boutiques", () => {
  render(<TopBar>{value}</TopBar>);
  const linkElement = screen.getByText(new RegExp(value, "i"));
  expect(linkElement).toBeInTheDocument();
});
