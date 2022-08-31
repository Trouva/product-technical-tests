import Image from "next/image";
import React from "react";
import { Logo, Wrapper } from "./Style";

const BoutiqueDetail = ({
  name,
  description,
  founder_quote,
  logo
}: Boutique) => (
  <Wrapper>
    <Logo>
      <Image src={logo?.url} alt={name} layout="fill" objectFit="contain" />
    </Logo>
    <h1>{name}</h1>
    <p>{description}</p>
    {founder_quote && <blockquote>{founder_quote}</blockquote>}
  </Wrapper>
);

export default BoutiqueDetail;
