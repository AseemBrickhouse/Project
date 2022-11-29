import React, { Component, useEffect, useState } from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";
import styles from "../Componenets/css/buttonGroupComponent.module.css";

const StudyGroupNav = () =>{
    return(
	    <div className={styles.container}>
		    <div className={styles.infoBox}>
		    <div className={styles.buttonGroup}>
			    <button className={styles.button}>Announcements</button>
			    <button className={styles.button}>Modules</button>
			    <button className={styles.button}>ChatRoom</button>
		    </div>
		    </div>
	    </div>
    )
}

export default StudyGroupNav;