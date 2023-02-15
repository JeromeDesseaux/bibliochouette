import * as React from 'react';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import  BookIcon from '@mui/icons-material/Book';
import PeopleIcon from '@mui/icons-material/People';
import {Link} from "react-router-dom"

export const mainListItems = (
    <React.Fragment>
        <ListItemButton component={Link} to="/dashboard">
            <ListItemIcon>
                <BookIcon/>
            </ListItemIcon>
            <ListItemText primary="Livres"/>
        </ListItemButton>
        <ListItemButton component={Link} to="/dashboard/groups">
            <ListItemIcon>
                <PeopleIcon/>
            </ListItemIcon>
            <ListItemText primary="Groupes"/>
        </ListItemButton>
        <ListItemButton component={Link} to="/dashboard/loans">
            <ListItemIcon>
                <ShoppingCartIcon/>
            </ListItemIcon>
            <ListItemText primary="Emprunts et retours"/>
        </ListItemButton>
    </React.Fragment>
);