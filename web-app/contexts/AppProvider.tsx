import { createContext, Dispatch, SetStateAction, useEffect, useState } from "react";

type AppContextValueProps = {
  location?: GeolocationCoordinates;
  showMap: boolean;
  setShowMap: Dispatch<SetStateAction<boolean>>;
};

export const AppContext = createContext({} as AppContextValueProps);

type AppProviderProps = {
  children: React.ReactNode;
};

export const AppProvider = ({ children }: AppProviderProps) => {
  const [showMap, setShowMap] = useState(false);
  const [location, setLocation] = useState<GeolocationCoordinates>();

  useEffect(() => {
    if (!navigator.geolocation) return;

    navigator.geolocation.getCurrentPosition(({ coords }) =>
      setLocation(coords)
    );
  }, []);

  return (
    <AppContext.Provider value={{ location, showMap, setShowMap }}>
      {children}
    </AppContext.Provider>
  );
};
