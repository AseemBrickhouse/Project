import React, { Component } from 'react';
import {Link} from 'react-router-dom';

const Login = (props) => {
    return (
    <body>
      <div class="container">
        <div class="login-box">
          <form class="login">
            <div class="elements">
              <h1>Login to your account</h1>
            </div>
            <div class="elements">
              <input type="text" placeholder="Username" id="username" class="inputBoxes" />
            </div>
            <div class="elements">
              <input type="password" placeholder="Password" id="password" class="inputBoxes" />
            </div>
            <div class="elements">
              <Link to = '/RecoveryPassword'>
                <a>Forgot Password</a>
              </Link>
              {/* <a href= "/Project/frontend/templates/frontend/login/forgotPassword.html">Forgot Password?</a> */}
            </div>
            <div class="elements">
              <button class="full-btn">Login</button>
            </div>
            <div class="elements">
                <Link to = '/CreateAccount'>
                    <button>
                        Sign up
                    </button>
                </Link>
              {/* <a href= "/Project/frontend/templates/frontend/createAccount/createAccount.html">Sign Up</a> */}
            </div>
          </form>
        </div>
      </div>
    </body>
    )
}

export default Login;
