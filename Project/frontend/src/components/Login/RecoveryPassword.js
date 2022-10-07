import React, { Component } from 'react';
import {Link} from 'react-router-dom';

const RecoveryPassword = (props) => {
    return (
        <body>
          <div class="container">
            <div class="login-box">
              <form class="login">
                <div class="elements">
                  <h1>Forgot Password?</h1>
                </div>
                <div class="elements">
                  <p>Enter your email assosiated with your acccount</p>
                </div>
                <div class="elements">
                  <input type="text" placeholder="Email" id="email" class="inputBoxes" />
                </div>
                <div class="elements">
                  <button onclick = "location.href='/Project/frontend/templates/frontend/login/recoveryMessage.html'" type="button">Recover Account</button>
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
export default RecoveryPassword;
