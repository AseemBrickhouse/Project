import React, { Component } from 'react';
import {Link, withRouter} from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from '../../store/actions/auth';
import {Button, Form, FormControl } from 'react-bootstrap';

const Login = (props) => {
    // const test = {
    //   username: "test1",
    //   password: "s8530216",
    // }
    console.log(props)

    const handleSubmit = (event) => {
      event.preventDefault();
      const data = new FormData(event.currentTarget);
      props.onAuth(data.get('username'), data.get('password'));

      setTimeout(()=>{
        props.history.push('/')
      }, 1000)
    }
    return (
      <body>
        <div className="container">
          <div className="login-box">
              <Form className="login" onSubmit={handleSubmit}>
                <div className="elements">
                  <h1>Login to your account</h1>
                </div>
                <div className="elements">
                  <FormControl
                    // className="inputBoxes"
                    id="username"
                    name="username"
                    type="text"
                    placeholder="Username"
                  />
                </div>
                <div className="elements">
                  <FormControl
                    id="password"
                    name="password"
                    type="password"
                    placeholder="Password"
                  />
                </div>
                <div className="elements">
                  <Link to = '/RecoveryPassword'>
                    <a>Forgot Password</a>
                  </Link>
                </div>
                <div className="elements">
                  <div component="form">
                    <button type="submit">
                      Login
                    </button>
                  </div>
                </div>
                <div className="elements">
                 <Link to = '/CreateAccount'>
                     <button>
                         Sign up
                     </button>
                 </Link>
                </div>
              </Form>
          </div>
        </div>
      </body>
      // <div>
      //   <Form className="container" onSubmit={handleSubmit}>
      //     {/* <CSRFToken/> */}
      //     <Form.Group>
      //       <FormControl
      //         type="text"
      //         name="username"
      //         id="username"
      //         value={test.username}
      //         placeHolder="Username"
      //       />
      //       <FormControl
      //         id="password"
      //         type="text"
      //         name="password"
      //         value={test.password}
      //         placeHolder="Password"
      //       />
      //     </Form.Group>
      //     <Button type="submit">
      //       Login
      //     </Button>
      //   </Form>
      // </div>
    // <body>
    //   <div class="container">
    //     <div class="login-box">
    //       <form class="login">
    //         <div class="elements">
    //           <h1>Login to your account</h1>
    //         </div>
    //         <div class="elements">
    //           <input type="text" placeholder="Username" id="username" class="inputBoxes" />
    //         </div>
    //         <div class="elements">
    //           <input type="password" placeholder="Password" id="password" class="inputBoxes" />
    //         </div>
    //         <div class="elements">
    //           <Link to = '/RecoveryPassword'>
    //             <a>Forgot Password</a>
    //           </Link>
    //           {/* <a href= "/Project/frontend/templates/frontend/login/forgotPassword.html">Forgot Password?</a> */}
    //         </div>
    //         <div class="elements">
    //           {/* <button class="full-btn">Login</button> */}
    //           <div component='form' noValidate onSubmit={handleSubmit}>
    //               <Button type="submit">
    //                 Login
    //               </Button>
    //           </div>
    //         </div>
    //         <div class="elements">
    //             <Link to = '/CreateAccount'>
    //                 <button>
    //                     Sign up
    //                 </button>
    //             </Link>
    //           {/* <a href= "/Project/frontend/templates/frontend/createAccount/createAccount.html">Sign Up</a> */}
    //         </div>
    //       </form>
    //     </div>
    //   </div>
    // </body>
    )
}

const mapStateToProps = (state) => {
  return{
    loading: state.auth.loading,
    error: state.auth.error,
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onAuth: (username, password) => dispatch(actions.authLogin(username, password))
  }
}
export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Login))
