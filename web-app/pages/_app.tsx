import type { AppProps } from "next/app";
import { AppProvider } from "../contexts/AppProvider";

const MyApp = ({ Component, pageProps }: AppProps) => (
  <AppProvider>
    <Component {...pageProps} />
  </AppProvider>
);

export default MyApp;
