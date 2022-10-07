import React, { Component } from 'react';
import {Link} from 'react-router-dom';

const AccountCreated = (props) => {
    return (
        <body>
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
                    <Link to= '/Login' style={{textDecoration: 'none'}}><button>Login</button></Link>
                    {/* <button onclick = "location.href='/Project/frontend/templates/frontend/login/login.html'" type="button">Login</button> */}
                    </div>
                </form>
                </div>
            </div>
        </body>
    );
}
export default AccountCreated;


// <!DOCTYPE html>
// <html lang="en">

// <head>
//   <meta charset="UTF-8">
//   <meta http-equiv="X-UA-Compatible" content="IE=edge">
//   <meta name="viewport" content="width=device-width, initial-scale=1.0">
//   <title>Account Created!</title>
//   <link rel="stylesheet" href="login.css">
// </head>

// <body>
//   <div class="container">
//     <div class="login-box">
//       <form class="login">
//         <div class="elements">
//           <h1>Account Created!</h1>
//         </div>
//         <div class="elements">
//           <p>Click the button below to login to your new account!</p>
//         </div>
//         <div class="elements">
//           <button onclick = "location.href='/Project/frontend/templates/frontend/login/login.html'" type="button">Login</button>
//         </div>
//       </form>
//     </div>
//   </div>
// </body>

// </html>

