import { Button } from "@mui/material"

export const SyncButton = ({entity, cb}) => {
    return (
        <Button onClick={cb}>Synchroniser les {entity}</Button>
    )

}