import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import {Link} from "react-router-dom"
export const NoItemError = ({itemName}) => {
    return (
        <Stack direction="column">
            Ooooops 😳 Apparemment, vous n'avez aucun {itemName} pour le moment.
            <Button variant="outlined" component={Link} to={'/book/add'}>Ajoutez votre premier {itemName}</Button>
        </Stack>
    )
}