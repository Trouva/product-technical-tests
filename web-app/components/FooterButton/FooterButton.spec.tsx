import { render, screen } from "@testing-library/react";
import FooterButton from ".";

const mock = {
  content: "MAIDEN",
};

test("renders FooterButton", () => {
  render(
    <FooterButton>
      {mock.content}
    </FooterButton>
  );

  const content = screen.getByText(new RegExp(mock.content, "i"));
  
  expect(content).toBeInTheDocument();
});
