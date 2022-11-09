import React, { Component } from 'react';
import {Link,  withRouter} from 'react-router-dom';
import * as actions from '../../store/actions/auth';
import {Button, Form, FormControl } from 'react-bootstrap';
import AccountCreated from './AccountCreated';
import { connect } from 'react-redux';

const CreateAccount = (props) => {
    const [load, setLoad] = React.useState(false)

    const infoCheck = (email, password1, password2) =>{
        if(password1 != password2){
          return false
        }
        //Check Other info
        return true
    }

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
            if(response = 200){
              //Success
            }else if(response > 200){
              //Error
            }
          })
          setLoad(false)
          props.history.push('/')
      }, 3000)
    }
    return(
      <div>
      {
        load ?
        <div>
          {/* Pass in correct info */}
          <AccountCreated/>
          {console.log("loading")}
          <></>
        </div>
        :
        <body>
          <div className="container">
            <div className="info-box">
              <Form clasName="info" onSubmit={handleSubmit}>
                <div className="elements">
                  <h1>Create your account</h1>
                </div>
                <div className="elements">
                  <FormControl
                    type="text"
                    placeholder="Username"
                    id="username"
                    name="username"
                    autoComplete="username"
                    // className="inputBoxes"
                  />
                </div>
                <div className="elements">
                  <FormControl
                    type="password"
                    placeholder="Password"
                    id="password1"
                    name="password1"
                    autoComplete="new-password"
                    // className="inputBoxes"
                  />
                  </div>
                  <div className="elements">
                  <FormControl
                    type="password"
                    placeholder="Confirm Password"
                    id="password2"
                    name="password2"
                    autoComplete="new-password"
                    // className="inputBoxes"
                  />
                  </div>
                  <div className="elements">
                  <FormControl
                    type="email"
                    placeholder="email"
                    id="email"
                    name="email"
                    autoComplete="email"
                    // className="inputBoxes"
                  />
                  </div>
                  <div className="elements">
                  <FormControl
                    type="text"
                    placeholder="Phone Number"
                    id="phone"
                    name="phone"
                    // className="inputBoxes"
                  />
                </div>
                <div className="elements">
                  <FormControl
                    type="text"
                    placeholder="First Name"
                    id="first_name"
                    name="first_name"
                    autoComplete="first_name"
                    // className="inputBoxes"
                  />
                </div>
                <div className="elements">
                  <FormControl
                    type="text"
                    placeholder="Last Name"
                    id="last_name"
                    name="last_name"
                    autoComplete="last_name"
                    // className="inputBoxes"
                  />
                </div>
                <div className="elements">
                  <button type="submit">
                      Create Account
                  </button>
                </div>
              </Form>
            </div>
          </div>
        </body>
      }
      </div>
    )
}
const mapStateToProps = (state) =>{
  return{
      loading: state.loading,
      error: state.error,
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