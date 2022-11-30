import React, { Component, useEffect, useState } from 'react';
import {Link } from 'react-router-dom';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";
import styles from "../Componenets/css/buttonGroupComponent.module.css";

const StudyGroupNav = (props) =>{
	console.log(props)
	const group = props.group
    return(
	    <div className={styles.container}>
		    <div className={styles.infoBox}>
		    <div className={styles.buttonGroup}>
				<Link 							
					style={{
					textDecoration: "none",
					color: "black",
					underline: "none",
					marginLeft: "-1%",
					}}
					to={{
					pathname: '/StudyGroupHome/' + group.studygroup_id + '/Announcements',
						state: { 
					  		studygroup_id: group.studygroup_id,
					  		group: group,
						},
					}}>
						<button className={styles.button}>Announcements</button>
				</Link>
				<Link 							
					style={{
					textDecoration: "none",
					color: "black",
					underline: "none",
					marginRight: "1%",
					marginLeft: "1%",
					}}
					to={{
					pathname: '/StudyGroupHome/' + group.studygroup_id + '/Modules',
						state: { 
					  		studygroup_id: group.studygroup_id,
					  		group: group,
						},
					}}>
						<button className={styles.button}>Modules</button>
				</Link>
				<Link 							
					style={{
					textDecoration: "none",
					color: "black",
					underline: "none",
					marginRight: "1%",
					}}
					to={{
					pathname: '/StudyGroupHome/' + group.studygroup_id + '/ChatRoom',
						state: { 
					  		studygroup_id: group.studygroup_id,
					  		group: group,
						},
					}}>
						<button className={styles.button}>ChatRoom</button>
				</Link>
		    </div>
		    </div>
	    </div>
    )
}

export default StudyGroupNav;