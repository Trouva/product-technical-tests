import type { AppProps } from "next/app";
import Head from "next/head";
import GlobalStyle from "../layout/GlobalStyle";
import { AppProvider } from "../contexts/AppProvider";
import { BoutiquesProvider } from "../contexts/BoutiquesProvider";
import 'react-loading-skeleton/dist/skeleton.css'

const MyApp = ({ Component, pageProps }: AppProps) => (
  <>
    <GlobalStyle />
    <Head>
      <title>Trouva Boutiques</title>
      <meta name="description" content="Trouva Boutiques" />
      <link rel="icon" href="/favicon.ico" />
    </Head>
    <AppProvider>
      <BoutiquesProvider>
        <Component {...pageProps} />
      </BoutiquesProvider>
    </AppProvider>
  </>
);

export default MyApp;