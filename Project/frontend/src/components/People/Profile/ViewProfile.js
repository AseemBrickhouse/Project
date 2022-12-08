import React, { Component, useEffect } from 'react';
import {Image} from 'react-bootstrap';
import styles from '../css/profile.module.css';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';

const ViewProfile = (props) => {
    let account = null
      if (props.location.state != null){
        account = props.location.state.person
      }else{
        account = props.account
      }
  
    console.log(account)
    return (
        <div className={styles.container}>
        <div className={styles.loginBox}>
          <div className={styles.tittle}>
            <h1 style={{color: "white"}}>User Account</h1>
          </div>
          <form className={styles.login}>
            <section>
              <span className={styles.icon}>
                {
                account.profile_pic != null ?
                <Image
                    src={account.profile_pic}
                    roundedCircle
                    width={200}
                    height={200}
                    style={{marginRight: "10px", marginLeft: "10px"}}
                />
                :
                <Image
                    src="https://cdn-icons-png.flaticon.com/512/2102/2102647.png"
                    roundedCircle
                    width={200}
                    height={200}
                    style={{marginRight: "10px", marginLeft: "10px"}}
                />
                }
              </span>
                <button className={styles.button}>{`${account.first_name}`}</button>
                <button className={styles.button}>{`${account.last_name}`}</button>
                <button className={styles.button}>{`${account.email}`}</button>
                <button className={styles.button}>{`${account.phone_number}`}</button>
                <button className={styles.button} href="/EnrolledStudyGroups">Study Groups</button>
                <button className={styles.button}>Meetings</button>
                {
                  props.location.state == null ?
                  <div className={styles.buttonGroup}>
                    <button className={styles.smallButton} href="/EditProfile/">Edit Profile</button>
                    <button className={styles.smallButton}>Close</button>
                  </div>
                  : null
                }
                {/* <div className={styles.buttonGroup}>
                  <button className={styles.smallButton}>Edit Profile</button>
                  <button className={styles.smallButton}>Close</button>
                </div> */}
            </section>
    
            {/* <div className="elements">
              <a href = "/Project/frontend/templates/frontend/login/login.html" className={styles.centeredLink}>Sign into another account</a>
            </div> */}
          </form>
        </div>
      </div>
    )
}

const mapStateToProps = (state) => {
    return {
        isAuthenticated: state.auth.token !== null,
        account: state.auth.account
    }
}
export default withRouter(connect(mapStateToProps, null)(ViewProfile));