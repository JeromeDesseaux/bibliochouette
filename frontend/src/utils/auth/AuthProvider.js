import React, {createContext, useState} from "react";

export const AuthContext = createContext({
    isAuthenticated: false,
    isLoading: true,
    login: () => {
    },
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

    return (
        <AuthContext.Provider value={{isAuthenticated, isLoading, login}}>
            {props.children}
        </AuthContext.Provider>
    )
}