import React, { HTMLAttributes, ReactNode } from "react";
import { Wrapper, Icon, Content } from "./Style";

interface Props extends HTMLAttributes<HTMLDivElement> {
  children: ReactNode;
  icon?: ReactNode;
  secondaryAction?: ReactNode;
}

const ListItem = ({ icon, secondaryAction, children, ...props }: Props) => (
  <Wrapper {...props}>
    {icon && <Icon>{icon}</Icon>}
    <Content>{children}</Content>
    {secondaryAction && secondaryAction}
  </Wrapper>
);

export default ListItem;
