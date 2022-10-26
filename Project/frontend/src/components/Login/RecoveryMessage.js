import React, { Component } from 'react';
import {Link} from 'react-router-dom';

const RecoveryMessage = (props) =>{
    return (
        <body>
          <div class="container">
            <div class="login-box">
              <form class="login">
                <div class="elements">
                  <p>Steps to recover your account have been sent to your email address.</p>
                </div>
                <div class="elements">
        			<button onclick = "location.href='/Project/frontend/templates/frontend/login/login.html'" type="button">Login</button>
                </div>
                <div class="elements">
                  <a href= "/Project/frontend/templates/frontend/createAccount/createAccount.html">Sign Up</a>
                </div>
              </form>
            </div>
          </div>
        </body>
    )
}
export default RecoveryMessage;
