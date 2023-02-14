import React from "react";

import {createBrowserRouter, RouterProvider,} from "react-router-dom";
import {createTheme, ThemeProvider} from '@mui/material/styles';

import Layout from "./components/Layout";
import Login from "./pages/Login";
import Register from "./pages/Register";

const router = createBrowserRouter([
    {
        path: "/login",
        element: <Login/>
    },
    {
        path: "/register",
        element: <Register/>
    },
    {
        path: "/",
        element: <Layout/>
    },
])

const theme = createTheme()

function App() {
    return (
        <React.StrictMode>
            <ThemeProvider theme={theme}>
                <RouterProvider router={router}/>
            </ThemeProvider>
        </React.StrictMode>
    );
}

export default App;
