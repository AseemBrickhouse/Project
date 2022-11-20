import React, { Component } from 'react';
import styles from "./css/group.module.css";

const GroupCard = (props) =>{
    return(
        // <body>
        	<div className={styles.containergroupcard}>
        		<div className={styles.infoboxgroupcard}>
        			<form className={styles.info}>
        				<div className={styles.Imgplaceholder}></div>
        				<h1 className={styles.center}>Group Name</h1>
        				<div className={styles.elements}>
        					<p className={styles.center}>This is the lengthy Description of the group yatta yatta yatta yatta yatta yatta yatta</p>
        				</div>
        				<div className={styles.footer}>
        					<div className={styles.button}>Create</div>
        					<div className={styles.button}>Create</div>
        				</div>
        			</form>
        		</div>
        	</div>
        // </body>
    )
}

export default GroupCard;