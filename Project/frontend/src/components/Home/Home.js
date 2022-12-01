import React, { Component, useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import FeedCard from './UserFeed/FeedCard';
import * as actions from "../../store/actions/auth";
import styles from "./UserFeed/Components/Feed css/feed.modules.css";
import { Info } from 'react-bootstrap-icons';
import SideBar from './Components/HomeSideBarLeft';

const Home = (props) => {
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
    console.log(feed)
    return (
        <div className={styles.containerhome}>
            <body className={styles.bodyhome}>
                <div className={styles.containerhome}>
                    <div className={styles.containerLeft}>
                        <SideBar/>
                    </div>
                    <div className={styles.containerMiddle}>
                    {
                        isAuthenticated ?
                            feed != null ?
                                <div className={styles.feedbody}>
                                {
                                    Object.entries(feed).map(([_, content]) => {
                                        return (
                                            <FeedCard {...content}/>
                                        )
                                    })
                                }
                                </div>
                            :
                            <div className={styles.feedbodyAlt}>
                                You have no current activity. Enroll in study groups, and meeetings to utilize this system!
                            </div>
                        : 
                        <div className={styles.feedbodyAlt}>
                            <h1>Name</h1>
                            <p>Providing connections to the things that matter.</p>
                        </div>
                    }
                    </div>
                    <div className={styles.containerRight}>

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