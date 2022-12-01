import React, { Component, useEffect, useState } from 'react';
import styles from "../css/sidebar.module.css"

const SideBar = (props) => {
    return(
    <div classNameName={styles.container}>
      <div className={styles.loginBox}>
        <div className={styles.title}>
          <h1>Quick Links</h1>
        </div>
        <form className={styles.login}>
          <section>
              <button className={styles.button}>Link 1</button>
              <button className={styles.button}>Link 2</button>
              <button className={styles.button}>Link 3</button>
              <button className={styles.button}>Link 4</button>
        
              <div className={styles.buttonGroup}>
                <button className={styles.smallButton}>Active Scholarships</button>
                <button className={styles.smallButton}>Active Study Groups</button>
    			  <button className={styles.smallButton}>Archive</button>
              </div>
          </section>
        </form>
      </div>
    </div>
    )
}

export default SideBar;