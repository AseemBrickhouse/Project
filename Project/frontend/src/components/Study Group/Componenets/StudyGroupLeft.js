import React, { Component, useEffect, useState } from 'react';
import styles from "../Componenets/css/StudyGroupInfoComponent.module.css";
import {Envelope} from "react-bootstrap-icons";
const StudyGroupLeft = (props) =>{
    // console.log(props)
    const group = props.group
    return(
        	<div className={styles.container}>
        		<div className={styles.infoBox}>
        			<h1 className={styles.tittle}>{`${group.studygroup_name}`}</h1>
        			<div className={styles.example}></div>
        			<div className={styles.imageCropper}>
        				<img src="https://sf1.autojournal.fr/wp-content/uploads/autojournal/2012/07/4503003e3c38bc818d635f5a52330d.jpg"  />
        			 </div>
        			<form className={styles.info}>
        				<div className={styles.bodyOwner}>{`Owner: ${group.studygroup_host.first_name} ${group.studygroup_host.last_name}`}</div>
        				<div className={styles.bodyDescription}>{`${group.studygroup_description}`}</div>
        			</form> 
					<div className={styles.footer}>
						<div className={styles.footerLeft}>Invites Out:</div>
						<div className={styles.footerRight}> 
							<Envelope/>
							<div>{`${group.invites_out}`}</div>
						</div>
					</div>
        			{/* <div className={styles.bottemsec}> 
					<div className={styles.footer}>
						Invites out: 
					</div>
        				<button className={styles.buttonbottom}>
        					Invites Out:
        				</button>
        				<button className={styles.smallbutton}>
        					icon
        				</button>
        			</div> */}
        		</div>
        	</div>
    )
}

export default StudyGroupLeft;