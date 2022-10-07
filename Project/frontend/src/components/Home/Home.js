import React, { Component } from 'react';
import Button from 'react-bootstrap';
import { Link } from 'react-router-dom';

const Home = (props) => { 
    console.log(props)
    return (
        <h1>
            Testing some code
            <Link to = "/CreateAccount">
                test
            </Link>
        </h1>   
    );
}
export default Home;