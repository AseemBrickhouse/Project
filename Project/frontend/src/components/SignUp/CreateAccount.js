import React, { Component, useState, useEffect, useRef } from 'react';
import {Link,  withRouter} from 'react-router-dom';
import * as actions from '../../store/actions/auth';
import {Button, Form, FormControl } from 'react-bootstrap';
import { connect } from 'react-redux';

import Overlay from 'react-bootstrap/Overlay';
import Tooltip from 'react-bootstrap/Tooltip';
import Alert from 'react-bootstrap/Alert';

import styles from "../Login/Componenets/css/login.module.css"
import Loading from '../Loadings/Login/Loading';

const CreateAccount = (props) => {
    const [load, setLoad] = useState(false);
    const [error, setError] = useState(false);
    const [update, setUpdate] = useState(null);

    const username = useRef(null);
    const password1 = useRef(null);
    const password2 = useRef(null);
    const email = useRef(null);

    const infoCheck = (email, password1, password2) =>{
        if(password1 != password2){
          return false
        }
        //Check Other info
        return true
    }

    useEffect(() => {
      if(!load && props.error != null){
        setError(!error)
        setUpdate(props.error)
      }else if (!load && props.error == null){
        // props.isAuthenticated ? props.history.push('/') : null
      }
    })

    const handleSubmit = (event) => {
      event.preventDefault()
      const data = new FormData(event.currentTarget);
      //Validate through infoCheck(data.get('email), data.get('password1'), data.get('password2'))
      props.onAuth(
        data.get('username'),
        data.get('email'),
        data.get('password1'),
        data.get('password2'),
      );
      setLoad(true)

      setTimeout(() =>{
          setLoad(false)
          props.error != null ? setError(true)
          :
          fetch("api/AccountCreation/" , {
            method: "POST",
            headers:{
              'Accept':'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              first_name: data.get('first_name'),
              last_name:data.get('last_name'),
              email: data.get('email'),
              phone: data.get('phone'),
              token: localStorage.getItem('token')
            })
          })
          .then(response => {
            if(response > 200){
              setError(!error)
            }
          })

          props.history.push('/')
      }, 3000)
    }
    return(
      <div>
      {
        load ?
          <Loading/>
        :
        // <body>
          <div className={styles.container}>
            <div className={styles.loginBox}>
              <Form clasName={styles.login} onSubmit={handleSubmit}>
                <div className={styles.elements}>
                  <h1>Create your account</h1>
                  {update != null && update.response.data.non_field_errors != null  ? 
                    <Alert variant='danger'><div><p>Two passwords did not match</p></div></Alert>: null
                  }
                </div>
                <div className={styles.elements}>
                  <FormControl
                    type="text"
                    placeholder="Username"
                    id="username"
                    name="username"
                    autoComplete="username"
                    ref={username}
                    // className="inputBoxes"
                  />
                    {
                      update != null && update.response.data.username != null ?
                      <Overlay target={username.current} show={true} placement="right-end">
                        {(props) => (
                            <Tooltip id="overlay-example" {...props}>
                              {`${update.response.data.username}`}
                            </Tooltip>
                          )}
                      </Overlay>
                      : null
                    }
                </div>
                <div className={styles.elements}>
                  <FormControl
                    type="password"
                    placeholder="Password"
                    id="password1"
                    name="password1"
                    autoComplete="new-password"
                    ref={password1}
                    // className="inputBoxes"
                  />
                  {
                      update != null && update.response.data.password1 != null ?
                      <Overlay target={password1.current} show={true} placement="right-end">
                        {(props) => (
                            <Tooltip id="overlay-example" {...props}>
                              {`${update.response.data.password1}`}
                            </Tooltip>
                          )}
                      </Overlay>
                      : null
                    }
                  </div>
                  <div className={styles.elements}>
                    <FormControl
                      type="password"
                      placeholder="Confirm Password"
                      id="password2"
                      name="password2"
                      autoComplete="new-password"
                      ref={password2}
                      // className="inputBoxes"
                    />
                    {
                      update != null && update.response.data.password2 != null ?
                      <Overlay target={password2.current} show={true} placement="right-end">
                        {(props) => (
                            <Tooltip id="overlay-example" {...props}>
                              {`${update.response.data.password2}`}
                            </Tooltip>
                          )}
                      </Overlay>
                      : null
                    }
                  </div>
                  <div className={styles.elements}>
                    <FormControl
                      type="email"
                      placeholder="email"
                      id="email"
                      name="email"
                      autoComplete="email"
                      ref={email}
                      // className="inputBoxes"
                    />
                    {
                      update != null && update.response.data.email != null ?
                      <Overlay target={email.current} show={true} placement="right-end">
                        {(props) => (
                            <Tooltip id="overlay-example" {...props}>
                              {`${update.response.data.email}`}
                            </Tooltip>
                          )}
                      </Overlay>
                      : null
                    }
                  </div>
                  <div className={styles.elements}>
                  <FormControl
                    type="text"
                    placeholder="Phone Number"
                    id="phone"
                    name="phone"
                    // className="inputBoxes"
                  />
                </div>
                <div className={styles.elements}>
                  <FormControl
                    type="text"
                    placeholder="First Name"
                    id="first_name"
                    name="first_name"
                    autoComplete="first_name"
                    // className="inputBoxes"
                  />
                </div>
                <div className={styles.elements}>
                  <FormControl
                    type="text"
                    placeholder="Last Name"
                    id="last_name"
                    name="last_name"
                    autoComplete="last_name"
                    // className="inputBoxes"
                  />
                </div>
                <div className={styles.elements}>
                  <button className={styles.button} type="submit">
                      Create Account
                  </button>
                </div>
              </Form>
            </div>
          </div>
        // </body>
      }
      </div>
    )
}
const mapStateToProps = (state) =>{
  return{
      loading: state.auth.loading,
      error: state.auth.error,
      isAuthenticated: state.auth.token !== null,
  }
}
const mapDispatchToProps = dispatch => {
  return {
    onAuth: (username, email, password1, password2) => dispatch(actions.authSignUp(username, email, password1, password2))
  }
}
export default withRouter(connect(mapStateToProps, mapDispatchToProps)(CreateAccount));


  // <body>
        //   <div class="container">
        //     <div class="info-box">
        //       <form class="info">
        //         <div class='elements'>
        //           <h1>Create your account</h1>
        //         </div>
        //         <div class="elements">
        //           <input type="text" placeholder="Username" id="username" class="inputBoxes" />
        //         </div>
        //         <div class="elements">
        //           <input type="password" placeholder="Password" id="password" class="inputBoxes" />
        //         </div>
        //         <div class="elements">
        // 			  <input type="text" placeholder="Email" id="email" class="inputBoxes" />
        // 		    </div>
        // 		    <div class="elements">
        // 		    	<input type="text" placeholder="Phone Number" id="phoneNumber" class="inputBoxes" />
        // 		    </div>
        // 		    <div class="elements">
        // 		    	<input type="text" placeholder="Street Adress" id="streetAddress" class="inputBoxes" />
        // 		    </div>
        // 		    <div class="elements">
        // 		    	<input type="text" placeholder="City" id="city" class="inputBoxes" />
        // 		    </div>
        // 		    <div class="elements">
        // 		    	<input type="text" placeholder="State" id="state" class="inputBoxes" />
        // 		    </div>
        // 		    <div class="elements">
        // 		    	<input type="text" placeholder="Zipcode" id="zipcode" class="inputBoxes" />
        // 		    </div>
        //         <div class="elements">
        //           <button class="full-btn">Create Account</button>
        //         </div>
        //       </form>
        //     </div>
        //   </div>
        // </body>