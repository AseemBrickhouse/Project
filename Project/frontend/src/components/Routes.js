import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";
import Home from './Home/Home';
import Login from '../components/Login/Login';
import Logout from '../components/Login/Logout';
import CreateAccount from '../components/SignUp/CreateAccount';
import AccountCreated from '../components/SignUp/AccountCreated';
import RecoveryMessage from '../components/Login/RecoveryMessage';
import RecoveryPassword from './Login/RecoveryPassword';

class Routes extends React.Component{
    render(){
        return(
        <React.Fragment>
            <Router>
                <Switch>
                    <Route exact path = "/"><Home/></Route>
                    
                    {/* /Login */}
                    <Route exact path = "/Login" component={Login}/>
                    <Route exact path = "/Logout" component={Logout}/>
                    <Route exact path = "/AccountCreated" component={AccountCreated}/>
                    <Route exact path = "/RecoveryMessage" component={RecoveryMessage}/>
                    <Route exact path = "/RecoveryPassword" component={RecoveryPassword}/>

                    {/* /SignUp */}
                    <Route exact path = "/AccountCreated" component={AccountCreated}/>
                    <Route exact path = "/CreateAccount" component={CreateAccount}/>
                </Switch>
            </Router>
        </React.Fragment>
        )
    }
}
export default Routes;