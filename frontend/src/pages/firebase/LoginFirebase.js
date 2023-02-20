import Box from '@mui/material/Box';
import { useContext } from 'react';
import { FirebaseAuthContext } from '../../utils/auth/FirebaseAuthProvider';
import { FirebaseSync } from './FirebaseSync';
import { LoginForm } from './LoginForm';


export const LoginFirebase = () => {
    const firebaseContext = useContext(FirebaseAuthContext);

    return (
        <Box>
            {
                firebaseContext.firebaseUser ? <FirebaseSync /> : <LoginForm />
            }
        </Box>
    )
}