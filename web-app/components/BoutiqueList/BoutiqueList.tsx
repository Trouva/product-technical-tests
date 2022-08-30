import Image from "next/image";
import Link from "next/link";
import React, { HTMLAttributes } from "react";
import { metersMask } from "../../utils/metersMask";
import ListItem, { ListItemPlaceHolder } from "../ListItem";
import { Wrapper } from "./Style";

interface Props extends HTMLAttributes<HTMLDivElement> {
  data: Boutique[];
  loading?: boolean;
}

const BoutiqueList = ({ loading, data = [], ...props }: Props) => (
  <Wrapper {...props}>
    {loading
      ? Array.from({ length: 5 }).map((_, index) => (
          <ListItemPlaceHolder key={index} icon secondaryAction />
        ))
      : data.map(
          ({ _id, description, name, founder_quote, logo, distance, slug }) => (
            <Link href={slug} passHref key={_id}>
              <a>
                <ListItem
                  icon={
                    <Image
                      src={logo.url}
                      alt={name}
                      layout="fill"
                      objectFit="contain"
                    />
                  }
                  secondaryAction={<div>{metersMask(distance)}</div>}
                >
                  <strong>{name}</strong>
                  <div>{description}</div>
                  {founder_quote && <em>{founder_quote}</em>}
                </ListItem>
              </a>
            </Link>
          )
        )}
  </Wrapper>
);

export default BoutiqueList;
