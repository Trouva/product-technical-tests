import axios, { AxiosError } from "axios";
import { useApp } from "../hooks/useApp";
import { useCallback, ReactNode, useMemo } from "react";
import { createContext, useEffect, useState } from "react";
import { useRouter } from "next/router";

interface BoutiquesContextValueProps {
  currentLocation?: GeolocationCoordinates;
  boutique: Boutique;
  boutiques: Boutique[];
  loading: boolean;
  error: string;
};

export const BoutiquesContext = createContext({} as BoutiquesContextValueProps);

interface BoutiquesProviderProps {
  children: ReactNode;
};

interface ErrorMessage {
  message: string;
};

export function BoutiquesProvider({ children }: BoutiquesProviderProps) {
  const { location } = useApp();
  const router = useRouter();
  const { slug } = router.query;

  const [boutiques, setBoutiques] = useState<Boutique[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const boutique = useMemo(() => boutiques.find((boutique) => boutique.slug === slug) || {} as Boutique, [boutiques.length, slug]);


  const getBoutiques = useCallback((lat: number, lon: number) => {
    setLoading(true);
    axios
      .get<Boutique[]>(
        `/api/boutiques?${new URLSearchParams({
          lat: `${lat}`,
          lon: `${lon}`,
        }).toString()}`
      )
      .then(({ data }) => setBoutiques(data))
      .catch((err: AxiosError<ErrorMessage>) =>
        setError(err.response?.data?.message || "Could not retrieve boutiques")
      )
      .then(() => setLoading(false));
  }, []);

  useEffect(() => {
    const { latitude, longitude } = location || {};
    if (!latitude || !longitude) return;

    getBoutiques(latitude, longitude);
  }, [location, getBoutiques]);

  return (
    <BoutiquesContext.Provider
      value={{
        currentLocation: location,
        boutique,
        boutiques,
        loading,
        error,
      }}
    >
      {children}
    </BoutiquesContext.Provider>
  );
}
