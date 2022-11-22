import React, { Component, useEffect }  from 'react';
import { BrowserRouter as Router } from "react-router-dom";
import { connect } from 'react-redux';
import Routes from './Routes';
import * as authActions from '../store/actions/auth';

const App = (props) => {
    const token = localStorage.getItem('token');
    // console.log(props)
    
    useEffect(() => {
        props.AutoTrySignUp();
    },[])

    return( 
        <React.Fragment>
            <Router>
                <Routes {...props}/>
            </Router>
        </React.Fragment>
    );
}

const mapStateToProps = (state) =>{
    return{
        account: state.auth.account,
        isAuthenticated: state.auth.token !== null,
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        AutoTrySignUp: () => dispatch(authActions.isValid()),
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(App);