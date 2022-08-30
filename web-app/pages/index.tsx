import type { NextPage } from "next";

import TopBar from "../components/Head";

import { useBoutiques } from "../hooks/useBoutiques";
import BoutiqueList from "../components/BoutiqueList";

const Home: NextPage = () => {
  const { boutiques, loading } = useBoutiques();
  return (
    <>
      <TopBar />
      <BoutiqueList loading={loading} data={boutiques} />
    </>
  );
};

export default Home;
