import axios, { AxiosError } from "axios";
import { NextApiRequest, NextApiResponse } from "next";
import { distanceTo, Location } from "geolocation-utils";

const API = process.env.API as string;
const PAGE_SIZE = 5;

const sortByDistance = (a: Boutique, b: Boutique) =>
  a.distance || 0 - b.distance || 0;

const handler = async (
  { method, query }: NextApiRequest,
  response: NextApiResponse<
    | Boutique[]
    | {
        message: string;
      }
  >
) => {
  const { lat, lon } = query as {
    lat: string;
    lon: string;
  };

  if (method !== "GET")
    return response.status(405).json({ message: "Unsupported method" });

  if (!lat || !lon)
    return response
      .status(400)
      .json({ message: "You should provide both latitude and longitude" });

  const distanceOfLocation = (location: Location) =>
    distanceTo(location, [+lon, +lat]);

  const parser = (boutique: APIBoutique) => ({
    ...boutique,
    logo: {
      url: "https://via.placeholder.com/32.png",
      ...boutique.logo,
    },
    distance: distanceOfLocation(boutique.location),
  });

  return axios
    .get<Boutique[]>(API)
    .then(({ data }) =>
      data.map(parser).sort(sortByDistance).slice(0, PAGE_SIZE)
    )
    .then((boutiques) => response.status(200).json(boutiques))
    .catch((err: AxiosError) =>
      response.status(err.response?.status || 500).json({
        message:
          (err.response?.data as string) || "Could not retrieve boutiques",
      })
    );
};

export default handler;
