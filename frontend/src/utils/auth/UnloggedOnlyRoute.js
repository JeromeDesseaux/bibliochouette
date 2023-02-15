import {AuthContext} from "./AuthProvider";
import {useContext} from "react";
import {Navigate, Outlet} from "react-router-dom";

export const UnloggedOnlyRoute = () => {
    const {isAuthenticated} = useContext(AuthContext);
    return isAuthenticated ? <Navigate to='/dashboard' replace/> : <Outlet/>
};