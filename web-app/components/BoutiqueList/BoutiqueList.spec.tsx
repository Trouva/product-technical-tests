import { render } from "@testing-library/react";
import BoutiqueList from ".";
import { boutiques } from "../../mock/boutiques";

describe("renders BoutiqueList", () => {
  it("Should render Placeholder", () => {
    const { container } = render(<BoutiqueList data={boutiques} loading />);
    const loading = container.getElementsByClassName("react-loading-skeleton");

    expect(loading.length).toBeTruthy();
  });

  it("Should render value", () => {
    const { container } = render(<BoutiqueList data={boutiques} />);
    const loading = container.getElementsByClassName("react-loading-skeleton");

    expect(loading.length).toBeFalsy();
    expect(container).toBeInTheDocument();
  });
});
