import React, {createContext, useState} from "react";
import { firebaseApp } from "../../firebase";
import {getAuth, signInWithEmailAndPassword} from "firebase/auth";


export const FirebaseAuthContext = createContext({
    firebaseUser: null,
    isLoading: true,
    error: null,
    login: () => {
    },
    logout: () => {
    }
});

export const FirebaseAuthProvider = props => {
    const [firebaseUser, setFirebaseUser] = useState(() => {
        const firebaseUser = localStorage.getItem("firebaseUser");
        return JSON.parse(firebaseUser);
    });
    const [isLoading, setLoading] = useState(false)
    const [error, setError] = useState(null)
    const auth = getAuth(firebaseApp);

    const login = (email, password) => {
        setLoading(true);

        signInWithEmailAndPassword(auth, email, password)
        .then(user => {
            setError(null)
            setFirebaseUser(user.user);
            localStorage.setItem("firebaseUser", JSON.stringify(user.user))
        })
        .catch(err => {
            setFirebaseUser(null);
            setError(err)
            localStorage.removeItem("firebaseUser");
        })
        .finally(() => setLoading(false));
    };

    const logout = () => {
        localStorage.removeItem("firebaseUser");
        window.location.reload(false);
    }

    return (
        <FirebaseAuthContext.Provider value={{firebaseUser, isLoading, error, login, logout}}>
            {props.children}
        </FirebaseAuthContext.Provider>
    )
}