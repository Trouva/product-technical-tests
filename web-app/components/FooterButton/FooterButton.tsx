import { HTMLAttributes, ReactNode } from "react";
import { Wrapper } from "./Style";

interface Props extends HTMLAttributes<HTMLSpanElement> {
  children: ReactNode;
}

export const FooterButton = ({ children, ...props }: Props) => (
  <Wrapper {...props}>{children}</Wrapper>
);

export default FooterButton;
