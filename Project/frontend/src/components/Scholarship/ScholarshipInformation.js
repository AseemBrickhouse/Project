import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";

import styles from "./Components/css/scholarshipApplication.module.css"

const ScholarShipInformation = (props) => {
    return (            
        // <body>
        <div className={styles.back}>
          <div className={styles.container}>
            <div className={styles.infoBox}>
              <form className={styles.info}>
                <div className={styles.elements}>
                  <h1>Scholarship Name</h1>
                  <p>Scholarship Provider Name</p>
                </div>
                <div className={styles.elements}>
                  <div className={styles.button}>Collapseable button</div>
                </div>
                <div className={styles.elements}>
                  <p>Scholarship Description: This is a cool one to apply for because it'll allow you to get money.</p>
                </div>
                <div className={styles.elements}>
                  <p>Scholarship Requirements:</p>
                  <p>&#8226; Requirement</p>
                  <p>&#8226; Requirement</p>
                  <p>&#8226; Requirement</p>
                </div>
            
                <div className={styles.elements}>
                  <div className={styles.button}>Apply!</div>
                </div>
              </form>
            </div>
          </div>
        </div>
        // </body>
    );
}

export default ScholarShipInformation;