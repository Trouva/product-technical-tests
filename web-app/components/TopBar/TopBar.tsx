import React, { ReactNode } from "react";
import Router from "next/router";
import { Content, Icon, Wrapper } from "./Style";

interface Props {
  children: ReactNode;
}

const TopBar = ({ children }: Props) => (
  <Wrapper>
    <Icon onClick={() => Router.back()}>◀</Icon>
    <Content>{children}</Content>
  </Wrapper>
);

export default TopBar;
