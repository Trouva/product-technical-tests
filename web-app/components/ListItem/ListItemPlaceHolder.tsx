import React, { HTMLAttributes } from "react";
import Skeleton from "react-loading-skeleton";
import { Wrapper, Icon, Content } from "./Style";

interface Props extends HTMLAttributes<HTMLDivElement> {
  icon: boolean;
  secondaryAction: boolean;
}

export const ListItemPlaceHolder = ({ icon, secondaryAction, className }: Props) => (
  <Wrapper className={className} >
    {icon && <Icon as={Skeleton} />}
    <Content>
      <Skeleton width="20rem" />
      <Skeleton width="40rem"/>
      <Skeleton width="30rem" />
    </Content>
    {secondaryAction && <Icon as={Skeleton} />}
  </Wrapper>
);

export default ListItemPlaceHolder;
