import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import { useContext, useState } from 'react';
import { FirebaseAuthContext } from '../../utils/auth/FirebaseAuthProvider';


export const LoginForm = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const firebaseContext = useContext(FirebaseAuthContext);

    const submitForm = e => {
        e.preventDefault();
        firebaseContext.login(email, password);
    }
    return (
        <Box>
            <Box component="form" sx={{
                '& > :not(style)': { m: 1, width: '25ch' },
            }}
                noValidate
                autoComplete="off"
                onSubmit={submitForm}>
                <TextField id="email" label="Email" variant="outlined" required onChange={(e) => setEmail(e.target.value)} />
                <TextField id="password" label="Mot de passe" variant="outlined" type="password" onChange={(e) => setPassword(e.target.value)} />
                <Button variant="contained" onClick={submitForm} type="submit">Se connecter</Button>
            </Box>
            {
                firebaseContext.error ? <div>Identifiants erronés. Veuillez vérifier les saisies et recommencer. En cas de problème, contactez le support.</div> : <div></div>
            }
            <div>

            </div>
        </Box>
    )
}