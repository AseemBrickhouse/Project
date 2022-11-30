import React, { Component } from 'react';
import {Button} from 'react-bootstrap';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from "../../store/actions/auth";

import styles from "./Componenets/css/login.module.css";

const Logout = (props) =>{
  const account = props.account
    return (
      // <body>
        <div className={styles.container}>
          <div className={styles.loginBox}>
            <div className={styles.title}>
              <h1>Logout of your account</h1>
            </div>
            <form class={styles.login}>
              <section>
                <span className={styles.icon}>
                  <img src="https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/default-avatar.png" />
                </span>
                <section className={styles.iconText}>
                  <h2>{`${account.first_name} ${account.last_name}`}</h2>
                  <p>{`${account.email}`}</p>
                </section>
              </section>
              <div className={styles.elements}>
                <Link to='/'>
                  <div className={styles.button} onClick={props.logout}>
                      Logout
                  </div>
                </Link>
                {/* <button onclick = "location.href='/Project/frontend/templates/frontend/login/login.html'" type="button">Logout</button> */}
              </div>
              <div className={styles.elements}>
                <div className = {styles.centerLink} href = "/Project/frontend/templates/frontend/login/login.html">Sign into another account</div>
              </div>
            </form>
          </div>
        </div>
      // </body>
    )
}
const mapStateToProps = (state) => {
  return{
      account: state.auth.account
  }
}
const mapDispatchToProps = dispatch => {
    return {
      logout : () => dispatch(actions.authLOGOUT())
    }
}
export default withRouter(connect(mapStateToProps,mapDispatchToProps)(Logout));
