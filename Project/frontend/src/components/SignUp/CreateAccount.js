import React, { Component } from 'react';
import {Link} from 'react-router-dom';

const CreateAccount = (props) => {
    return(
        <body>
          <div class="container">
            <div class="info-box">
              <form class="info">
                <div class="elements">
                  <h1>Create your account</h1>
                </div>
                <div class="elements">
                  <input type="text" placeholder="Username" id="username" class="inputBoxes" />
                </div>
                <div class="elements">
                  <input type="password" placeholder="Password" id="password" class="inputBoxes" />
                </div>
                <div class="elements">
        			<input type="text" placeholder="Email" id="email" class="inputBoxes" />
        		</div>
        		<div class="elements">
        			<input type="text" placeholder="Phone Number" id="phoneNumber" class="inputBoxes" />
        		</div>
        		<div class="elements">
        			<input type="text" placeholder="Street Adress" id="streetAddress" class="inputBoxes" />
        		</div>
        		<div class="elements">
        			<input type="text" placeholder="City" id="city" class="inputBoxes" />
        		</div>
        		<div class="elements">
        			<input type="text" placeholder="State" id="state" class="inputBoxes" />
        		</div>
        		<div class="elements">
        			<input type="text" placeholder="Zipcode" id="zipcode" class="inputBoxes" />
        		</div>
                <div class="elements">
                  <button class="full-btn">Create Account</button>
                </div>
              </form>
            </div>
          </div>
        </body>
    )
}
export default CreateAccount;