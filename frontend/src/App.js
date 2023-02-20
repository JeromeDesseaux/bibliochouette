import React from "react";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { AuthProvider } from "./utils/auth/AuthProvider";
import { AppRouter } from "./utils/Router";
import { BrowserRouter } from "react-router-dom";
import { FirebaseAuthProvider } from "./utils/auth/FirebaseAuthProvider";


const theme = createTheme()

function App() {
    return (
        <React.StrictMode>
            <BrowserRouter>
                <AuthProvider>
                    <FirebaseAuthProvider>
                        <ThemeProvider theme={theme}>
                            <AppRouter />
                        </ThemeProvider>
                    </FirebaseAuthProvider>
                </AuthProvider>
            </BrowserRouter>
        </React.StrictMode>
    );
}

export default App;
