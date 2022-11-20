import React, { Component, useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import FeedCard from './UserFeed/FeedCard';
import * as actions from "../../store/actions/auth";
import styles from "./UserFeed/Components/Feed css/feed.modules.css";

const Home = (props) => {
    console.log(props)
    const isAuthenticated = props.isAuthenticated
    const [load, setLoad] = useState(false)
    const [feed, setFeed] = useState(null)
    useEffect(() => {
        if (!load){
            fetch("http://127.0.0.1:8000/api/GetUserFeed/", {
                method: "POST",
                headers: {
                    'Accept':'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    token: localStorage.getItem('token')
                })
            })
            .then(response => {
                return response.json()
            })
            .then(data =>{
                setLoad(true)
                setFeed(data)
            })
        }
    },[load])
    
    return (
        <div className={styles.containerhome}>
            <body className={styles.bodyhome}>
                <div className={styles.containerhome}>
                    <div className={styles.loginBox} >
                        <div className={styles.login}>
                            {
                                isAuthenticated ?
                                    feed != null ?
                                        <div className={styles.feedbody}>
                                        {
                                            Object.entries(feed).map(([id, content]) => {
                                                return (
                                                    <FeedCard {...content}/>
                                                )
                                            })
                                        }
                                        </div>
                                    : null
                                : 
                                <div>
                                    <h1>Name</h1>
                                    <p>Providing connections to the things that matter.</p>
                                </div>
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