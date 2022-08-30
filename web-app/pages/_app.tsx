import type { AppProps } from "next/app";
import { AppProvider } from "../contexts/AppProvider";
import { BoutiquesProvider } from "../contexts/BoutiquesContext";

const MyApp = ({ Component, pageProps }: AppProps) => (
  <AppProvider>
    <BoutiquesProvider>
      <Component {...pageProps} />
    </BoutiquesProvider>
  </AppProvider>
);

export default MyApp;
