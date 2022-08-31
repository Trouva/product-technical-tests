import React from "react";
import Skeleton from "react-loading-skeleton";
import { Wrapper, Logo } from "./Style";

export const BoutiqueDetailPlaceHolder = () => (
  <Wrapper>
    <Logo as={Skeleton} />
    <h1>
      <Skeleton width="20rem" />
    </h1>
    <p>
      <Skeleton count={3} />
      <Skeleton width="10rem" />
    </p>
  </Wrapper>
);

export default BoutiqueDetailPlaceHolder;
