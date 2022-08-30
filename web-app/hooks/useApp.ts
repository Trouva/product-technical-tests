import { AppContext } from "../contexts/AppProvider";
import { useContext } from "react";

export const useApp = () => useContext(AppContext);
