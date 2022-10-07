import React, { Component } from 'react';
import {Link} from 'react-router-dom';

const Logout = (props) =>{
    return (
        <body>
          <div class="container">
            <div class="login-box">
              <div class="tittle">
                <h1>Logout of your account</h1>
              </div>
              <form class="login">
                <section>
                  <span class="icon">
                    <img src="https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/default-avatar.png" />
                  </span>
                  <section class="icon-text">
                    <h2>Mahmoud Hammad</h2>
                    <p>mahmoudhammad243@gmail.com</p>
                  </section>
                </section>
                <div class="elements">
                  <button onclick = "location.href='/Project/frontend/templates/frontend/login/login.html'" type="button">Logout</button>
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
export default Logout;
