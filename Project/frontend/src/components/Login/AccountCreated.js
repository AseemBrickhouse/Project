import React, { Component } from 'react';
import {Link} from 'react-router-dom';

const AccountCreated = (props) =>{
    return (
        // <body>
          <div class="container">
            <div class="login-box">
              <form class="login">
                <div class="elements">
                  <h1>Account Created!</h1>
                </div>
                <div class="elements">
                  <p>Click the button below to login to your new account!</p>
                </div>
                <div class="elements">
                    <Link to ='/Login'>
                        <button>
                            Login
                        </button>
                    </Link>
                  {/* <button onclick = "location.href='/Project/frontend/templates/frontend/login/login.html'" type="button">Login</button> */}
                </div>
              </form>
            </div>
          </div>
        // </body>
    )
}
export default AccountCreated;
