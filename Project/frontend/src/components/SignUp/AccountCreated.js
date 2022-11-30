import React, { Component } from 'react';
import {Link} from 'react-router-dom';
import styles from "../Login/Componenets/css/login.module.css"
const AccountCreated = (props) => {
    return (
        <body>
            <div className={styles.container}>
                <div class={styles.loginBox}>
                <form class={styles.login}>
                    <div class={styles.elements}>
                    <h1>Account Created!</h1>
                    </div>
                    <div class={styles.elements}>
                    <p>Click the button below to login to your new account!</p>
                    </div>
                    <div class={styles.elements}>
                    <Link to= '/Login' style={{textDecoration: 'none'}}><div className={styles.button}>Login</div></Link>
                    {/* <button onclick = "location.href='/Project/frontend/templates/frontend/login/login.html'" type="button">Login</button> */}
                    </div>
                </form>
                </div>
            </div>
        </body>
    );
}
export default AccountCreated;
