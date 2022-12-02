import React, { Component, useState, useEffect } from 'react';
import styles from "./css/group.module.css";
import {Link} from 'react-router-dom'

const GroupCard = (props) =>{
	const [group, setGroup] = useState(props);
    const [load, setLoad] = useState(false);
	const [error, setError] = useState(false);

	useEffect(() => {
		if(load){
			fetch("/api/GetStudyGroup/",{
				method: "POST",
				headers:{
					'Accept':'application/json',
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					token: localStorage.getItem('token'),
					studygroup_id: group.studygroup_id,
				})
			})
			.then(response=> {
				return response.json();
			})
			.then(data=>{
				if(data.Message != null){
					setError(true)
				}else{
					setGroup(data)
				}
				setLoad(false)
			})
		}
    },[load]);

	const handleJoin = (studygroup) => {
		console.log(studygroup);
		fetch("api/JoinStudyGroup/", {  
			method: "POST",
			headers:{
				'Accept':'application/json',
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				token: localStorage.getItem('token'),
				studygroup_id: studygroup.studygroup_id,
			})
		})
		.then(response=>{
			return response.json()
		})
		.then(data=>{
			setLoad(true)
		})
	}

	const handleLeave = (studygroup) => {
		fetch("api/LeaveStudyGroup/", {  
			method: "DELETE",
			headers:{
				'Accept':'application/json',
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				token: localStorage.getItem('token'),
				studygroup_id: studygroup.studygroup_id,
			})
		})
		.then(response=>{
			return response.json()
		})
		.then(data=>{
			setLoad(true)
		})
	}

    return(
		<div>
			{
				!error ? 
				<div className={styles.containergroupcard}>
					<div className={styles.infoboxgroupcard}>
						<form className={styles.info}>
							<div className={styles.Imgplaceholder}></div>
							<h1 className={styles.center} style={{fontSize: "24px"}}>{group.studygroup_name}</h1>
							<div className={styles.elements}>
								<p className={styles.center}>{group.studygroup_description}</p>
							</div>
							<div className={styles.footer}>
								<Link
									style={{
									textDecoration: "none",
									color: "black",
									underline: "none",
									marginLeft: "10%"
									}}
									to={{
									pathname: '/StudyGroupHome/' + group.studygroup_id + '/',
										state: { 
											  studygroup_id: group.studygroup_id,
											  group: group,
										},
									}}>
									<div className={styles.button} style={{backgroundColor: "#A7916D"}}>View</div>
								</Link>
								{
									group.is_enrolled ? 
										<div className={styles.button} style={{backgroundColor: "#A04848", marginRight: "10%"}} onClick={() => handleLeave(group)}>Leave</div>
									:
										<div className={styles.button} style={{backgroundColor: "#A7916D", marginRight: "10%"}} onClick={() => handleJoin(group)}>Join</div>
								}
							</div>
						</form>
					</div>
				</div>
				: null
			}
		</div>
    )
}

export default GroupCard;