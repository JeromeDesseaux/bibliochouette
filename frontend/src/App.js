import React from "react";
import {createTheme, ThemeProvider} from '@mui/material/styles';
import {AuthProvider} from "./utils/auth/AuthProvider";
import {AppRouter} from "./utils/Router";
import {BrowserRouter} from "react-router-dom";


const theme = createTheme()

function App() {
    return (
        <React.StrictMode>
            <AuthProvider>
                <ThemeProvider theme={theme}>
                    <BrowserRouter>
                        <AppRouter/>
                    </BrowserRouter>
                </ThemeProvider>
            </AuthProvider>
        </React.StrictMode>
    );
}

export default App;
