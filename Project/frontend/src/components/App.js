import React, { Component }  from 'react';
import { BrowserRouter as Router } from "react-router-dom";
import Routes from './Routes';

class App extends Component{
    render(){
        return( 
            <React.Fragment>
                <Router>
                    <Routes {...this.props}/>
                </Router>
            </React.Fragment>
        );
    }
}
export default App;