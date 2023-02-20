// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
// Your web app's Firebase configuration

const firebaseConfig = {
    apiKey: "AIzaSyA-qYJ0KfrfORlgoiCZ5LWE2gHecCf1ms0",
    authDomain: "bibliochouette-7568c.firebaseapp.com",
    databaseURL: "https://bibliochouette-7568c.firebaseio.com",
    projectId: "bibliochouette-7568c",
    storageBucket: "bibliochouette-7568c.appspot.com",
    messagingSenderId: "554944219261",
    appId: "1:554944219261:web:59c1870b3a3e5ed22e0914"
};

// Initialize Firebase
export const firebaseApp = initializeApp(firebaseConfig);
export const firebaseDb = getDatabase(firebaseApp);
