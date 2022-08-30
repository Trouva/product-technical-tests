import { render, screen } from "@testing-library/react";
import ListItem from "./";

const mock = {
  content: "MAIDEN",
  secondaryAction: <span>secondary value</span>,
  icon: <span> icon</span>
};

test("renders ListItem", () => {
  render(
    <ListItem icon={mock.icon} secondaryAction={mock.secondaryAction}>
      {mock.content}
    </ListItem>
  );

  const content = screen.getByText(new RegExp(mock.content, "i"));
  const secondaryAction = screen.getByText(new RegExp(mock.content, "i"));
  const icon = screen.getByText(new RegExp(mock.content, "i"));
  
  expect(content).toBeInTheDocument();
  expect(secondaryAction).toBeInTheDocument();
  expect(icon).toBeInTheDocument();
});
