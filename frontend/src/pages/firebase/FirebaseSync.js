import { SyncButton } from "./SyncButton"
import Box from '@mui/material/Box';
import { Typography } from "@mui/material";
import { useContext } from "react";
import { FirebaseAuthContext } from "../../utils/auth/FirebaseAuthProvider";
import { ref, child, get } from "firebase/database";
import { firebaseDb } from "../../firebase";

export const FirebaseSync = () => {

    const firebaseContext = useContext(FirebaseAuthContext)

    const syncBooks = () => {
        const uuid = firebaseContext.firebaseUser.uid;

        const dbRef = ref(firebaseDb);
        get(child(dbRef, `books/${uuid}`)).then((snapshot) => {
            if (snapshot.exists()) {
                console.log(snapshot.val());
            } else {
                console.log("No data available");
            }
        }).catch((error) => {
            console.error(error);
        });
    }

    return (
        <Box>
            <Typography>Vous pouvez transférer les ouvrages enregistrés sur l'application Bibliochouette en cliquant sur le bouton ci-dessus. </Typography>
            <Typography>Attention : Cet import n'est à réaliser qu'une seule fois. Soyez patient, cela peut durer quelques minutes.</Typography>
            <Typography>Attention : La synchronisation n'est pas bilatérale. L'application Bibliochouette n'est plus supportée. Les ouvrages modifiés sur l'application ne seront pas modifiés ici.</Typography>
            <SyncButton entity="livres" cb={syncBooks} />
        </Box>
    )

}