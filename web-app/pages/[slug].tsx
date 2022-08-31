import type { NextPage } from "next";

import { useBoutiques } from "../hooks/useBoutiques";
import TopBar from "../components/TopBar";
import BoutiqueDetail, { BoutiqueDetailPlaceHolder } from "../components/BoutiqueDetail";
import { useRouter } from "next/router";

const Home: NextPage = () => {
  const { boutique, loading } = useBoutiques();
  const router = useRouter();

  return (
    <>
      <TopBar>{boutique?.name || router.query.slug }</TopBar>
        {loading ? (
          <BoutiqueDetailPlaceHolder />
        ) : (
          <BoutiqueDetail {...boutique} />
        )}
    </>
  );
};

export default Home;
