import React from "react";
import {createTheme, ThemeProvider} from '@mui/material/styles';
import {AuthProvider} from "./utils/auth/AuthProvider";
import {AppRouter} from "./utils/Router";
import {BrowserRouter} from "react-router-dom";


const theme = createTheme()

function App() {
    return (
        <React.StrictMode>
            <BrowserRouter>
                <AuthProvider>
                    <ThemeProvider theme={theme}>
                        <AppRouter/>
                    </ThemeProvider>
                </AuthProvider>
            </BrowserRouter>
        </React.StrictMode>
    );
}

export default App;
