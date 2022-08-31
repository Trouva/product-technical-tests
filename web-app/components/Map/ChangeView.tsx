import { useMap } from "react-leaflet";
import { useEffect } from "react";

interface Props {
  center?: GeolocationCoordinates;
}

const ChangeView = ({ center }: Props) => {
  const map = useMap();

  useEffect(() => {
    const { latitude, longitude } = center || {};
    if (!latitude || !longitude) return;

    map.setView([latitude, longitude], map.getZoom());
  }, [center, map]);

  return null;
};

export default ChangeView;
