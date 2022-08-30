import { useState } from "react";
import type { NextPage } from "next";
import dynamic from "next/dynamic";

import FooterButton from "../components/FooterButton";
import TopBar from "../components/Head";
import BoutiqueList from "../components/BoutiqueList";

import { useBoutiques } from "../hooks/useBoutiques";
import { useApp } from "../hooks/useApp";

const Map = dynamic(() => import("../components/Map"), { ssr: false });

const Home: NextPage = () => {
  const { showMap, setShowMap } = useApp();
  const { currentLocation, boutiques, loading } = useBoutiques();

  return (
    <>
      <TopBar />
      {showMap ? (
        <Map center={currentLocation} data={boutiques} />
      ) : (
        <BoutiqueList loading={loading} data={boutiques} />
      )}
      <FooterButton onClick={() => setShowMap((e) => !e)}>
        <b>Show as {!showMap ? "Map 📍" : "List"}</b>
      </FooterButton>
    </>
  );
};

export default Home;
