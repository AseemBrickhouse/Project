import React, { Component,useState, useEffect } from 'react';
import {Link, withRouter} from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from '../../store/actions/auth';
import {Button, Form, FormControl } from 'react-bootstrap';
import Loading from "../Loadings/Login/Loading";
import styles from "./Componenets/css/login.module.css";

const Login = (props) => {
    const [error, setError] = useState(null);
    const [load, setLoad] = useState(false);

    useEffect(()=>{
      setError(props.error)
    }, [load])

    const handleSubmit = (event) => {
      event.preventDefault();
      const data = new FormData(event.currentTarget);
      props.onAuth(data.get('username'), data.get('password'));
      setLoad(true);
      console.log(props)
      setTimeout(()=>{
        setLoad(false); 
        if(props.error != null){
          setLoad(false); 
          setError(true);
        }else{
          props.isAuthenticated ? props.history.push('/') : setError(true);
        }
      }, 3000)
    }
    return (
      <div>
      {
        load ? 
          <div>
            <Loading/>
          </div>
        :
      <body>
      <div className={styles.container}>
        <div className={styles.loginBox}>
            <Form className={styles.login} onSubmit={handleSubmit}>
              <div className={styles.elements}>
                <h1>Login to your account</h1>
                {error ? <div>
                <p>Invalid Username and/or password</p>
                </div> : null}
              </div>
              <div className={styles.elements}>
                <FormControl
                  id="username"
                  name="username"
                  type="text"
                  placeholder="Username"
                />
              </div>
              <div className={styles.elements}>
                <FormControl
                  id="password"
                  name="password"
                  type="password"
                  placeholder="Password"
                />
              </div>
              <div className={styles.elements}>
                <Link to = '/RecoveryPassword'>
                  <div className={styles.a}>Forgot Password</div>
                </Link>
              </div>
              <div className={styles.elements}>
                <div component="form">
                  <button className={styles.button} type="submit">
                    Login
                  </button>
                </div>
              </div>
              <div className={styles.elements}>
               <Link to = '/CreateAccount'>
                  <div className={styles.button}>
                      Sign up
                  </div>
               </Link>
              </div>
            </Form>
        </div>
      </div>
    </body>
      }
    </div>
    )
}

const mapStateToProps = (state) => {
  return{
    loading: state.auth.loading,
    isAuthenticated: state.auth.token != null,
    error: state.auth.error,
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onAuth: (username, password) => dispatch(actions.authLogin(username, password))
  }
}
export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Login))
