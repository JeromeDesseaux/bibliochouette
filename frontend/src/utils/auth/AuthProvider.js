import React, {createContext, useState} from "react";

export const AuthContext = createContext({
    isAuthenticated: false,
    isLoading: true,
    login: () => {
    },
    logout: () => {
    }
});

export const AuthProvider = props => {
    const [isAuthenticated, setAuthenticated] = useState(() => {
        const token = localStorage.getItem("tokens");
        return token !== null;
    });
    const [isLoading, setLoading] = useState(false)

    const login = () => {
        setLoading(false);
        setAuthenticated(true);
        localStorage.setItem("tokens", JSON.stringify({
            jwtToken: "blablabla",
            refreshToken: "blablabla"
        }))
    };

    const logout = () => {
        localStorage.removeItem("tokens");
        window.location.reload(false);
    }

    return (
        <AuthContext.Provider value={{isAuthenticated, isLoading, login, logout}}>
            {props.children}
        </AuthContext.Provider>
    )
}