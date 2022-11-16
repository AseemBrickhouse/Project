import React, { Component } from 'react';
import {Button} from 'react-bootstrap';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from "../../store/actions/auth";

const Logout = (props) =>{
  const account = props.account
    return (
      <body>
        <div class="container">
          <div class="login-box">
            <div class="title">
              <h1>Logout of your account</h1>
            </div>
            <form class="login">
              <section>
                <span class="icon">
                  <img src="https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/default-avatar.png" />
                </span>
                <section class="icon-text">
                  <h2>{`${account.first_name} ${account.last_name}`}</h2>
                  <p>{`${account.email}`}</p>
                </section>
              </section>
              <div class="elements">
                <Link to='/'>
                  <button onClick={props.logout}>
                      Logout
                  </button>
                </Link>
                {/* <button onclick = "location.href='/Project/frontend/templates/frontend/login/login.html'" type="button">Logout</button> */}
              </div>
              <div class="elements">
                <a href = "/Project/frontend/templates/frontend/login/login.html" class = "centered-link">Sign into another account</a>
              </div>
            </form>
          </div>
        </div>
      </body>
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
