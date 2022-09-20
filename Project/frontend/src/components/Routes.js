import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";
import Home from './Home/Home';

class Routes extends React.Component{
    render(){
        return(
        <React.Fragment>
            <Router>
                <Switch>
                    <Route exact path="/">
                        <Home/>
                    </Route>
                </Switch>
            </Router>
        </React.Fragment>
        )
    }
}
export default Routes;