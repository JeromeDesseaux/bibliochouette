import {Route, Routes} from "react-router-dom"
import {ProtectedRoute} from "./auth/ProtectedRoute";
import Login from "../pages/Login";
import Register from "../pages/Register";
import DashboardLayout from "../components/DashboardLayout";
import {UnloggedOnlyRoute} from "./auth/UnloggedOnlyRoute";
import {BookList} from "../pages/books/BookList";
import {GroupList} from "../pages/groups/GroupList";
import {LoanList} from "../pages/loans/LoanList";
import {NotFoundPage} from "../pages/errors/NotFound";
import {AddBook} from "../pages/books/AddBook";
import {EditBook} from "../pages/books/EditBook";
import {LoginFirebase} from "../pages/firebase/LoginFirebase";

export const AppRouter = () => {
    return (
        <Routes>
            <Route path='*' element={<NotFoundPage />}/>
            <Route element={<UnloggedOnlyRoute/>}>
                <Route path='/login' element={<Login/>}/>
                <Route path='/register' element={<Register/>}/>
            </Route>
            <Route element={<ProtectedRoute/>}>
                <Route element={<DashboardLayout/>}>
                    <Route
                        path="/dashboard"
                    >
                        <Route
                            index
                            element={(
                                <BookList/>
                            )}
                        />
                        <Route path="/dashboard/groups" element={<GroupList/>}></Route>
                        <Route path="/dashboard/loans" element={<LoanList/>}></Route>
                    </Route>
                    <Route path="/book/add" element={<AddBook/>}></Route>
                    <Route path="/book/edit" element={<EditBook/>}></Route>
                    <Route path="/firebase/login" element={<LoginFirebase/>}></Route>
                </Route>
            </Route>
        </Routes>
    );
}