import { useRouter } from "next/router";
import { MapContainer, TileLayer, Marker } from "react-leaflet";

import { Wrapper, Container } from "./styles";
import ChangeView from "./ChangeView";

interface Props{
  data?: Boutique[];
  center?: GeolocationCoordinates;
};

const Map = ({ data, center }: Props) => {
  const router = useRouter();

  return (
    <Wrapper>
      <Container
        as={MapContainer}
        minZoom={2}
        zoom={8}
        center={[center?.latitude || 0, center?.longitude || 0]}
        maxBounds={[
          [-180, 180],
          [180, -180],
        ]}
      >
        <ChangeView center={center} />
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {data?.map(({ _id, slug, name, location: { lat, lon } }) => (
          <Marker
            key={_id}
            position={[lat, lon]}
            title={name}
            riseOnHover
            eventHandlers={{
              click: () => router.push(slug),
            }}
          />
        ))}
      </Container>
    </Wrapper>
  );
};

export default Map;
