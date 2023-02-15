import {Route, Routes} from "react-router-dom"
import {ProtectedRoute} from "./auth/ProtectedRoute";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Layout from "../components/Layout";
import {UnloggedOnlyRoute} from "./auth/UnloggedOnlyRoute";

export const AppRouter = () => {
    return (
        <Routes>
            <Route index element={<Login/>}/>
            <Route element={<UnloggedOnlyRoute/>}>
                <Route path='/login' element={<Login/>}/>
                <Route path='/register' element={<Register/>}/>
            </Route>
            <Route element={<ProtectedRoute/>}>
                <Route
                    path="/dashboard"
                >
                    <Route
                        index
                        element={(
                            <Layout/>
                        )}
                    />
                </Route>
            </Route>
        </Routes>
    );
}