import {AuthContext} from "./AuthProvider";
import {useContext} from "react";
import {Outlet, Navigate} from "react-router-dom";

export const ProtectedRoute = () => {
  const {isAuthenticated, isLoading} = useContext(AuthContext);
  
  if (isLoading) {
    return <section>Chargement...</section>;
  }
  return !isAuthenticated ? <Navigate to='/login' replace /> : <Outlet />
};