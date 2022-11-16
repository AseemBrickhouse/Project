import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from "../../store/actions/auth";

const Home = (props) => {
    console.log(props)
    const isAuthenticated = props.isAuthenticated
    return (
        <div className='containerhome'>
{/*             
            <div class="navContainer">
                <div class="navigation">
                    <li><a href="/home/">Students</a></li>
                    <li><a href="/courses/">Instructors</a></li>
                    <li><a href="/users/">Tutors</a></li>
                    <li><a href="/">Logout</a></li>
                </div>
            </div> */}
            <body className='bodyhome'>
                <div className="containerhome">
                    <div className="login-box" >
                        <div className="login">
                                <h1>Name</h1>
                                <p>Providing connections to the things that matter.</p>
                            {
                                !isAuthenticated ?
                                    <div>
                                        <div className='elements'>
                                            <Link to="/Login">
                                                <button type="submit">
                                                    Login
                                                </button>
                                            </Link>
                                        </div>
                                            <p>New here?</p>
                                        <div>
                                            <Link to="/Login">
                                                <button type="submit">
                                                    Get Started
                                                </button>
                                            </Link>
                                        </div>
                                    </div>
                                    :
                                    <Link to='/Logout'>
                                        <button type="submit">
                                            Logout
                                        </button>
                                    </Link>
                            }
                        </div>
                    </div>
                </div>
            </body>
        </div>
    );
}
const mapStateToProps = (state) => {
    return {
        isAuthenticated: state.auth.token !== null,
        account: state.auth.account
    }
}
const mapDispatchToProps = dispatch => {
    return {
        logout: () => dispatch(actions.authLOGOUT())
    }
}
export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Home));