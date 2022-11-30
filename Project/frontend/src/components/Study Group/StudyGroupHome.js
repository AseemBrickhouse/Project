import React, { Component, useEffect, useState } from 'react';
import GroupCard from './Componenets/GroupCard';
import styles from "./Componenets/css/StudyGroupLayout.module.css";
import StudyGroupLeft from './Componenets/StudyGroupLeft';
import StudyGroupMiddle from './Componenets/StudyGroupMiddle';
import StudyGroupRight from './Componenets/StudyGroupRight';

const StudyGroupHome = (props) =>{
    const [modules, setModules] = React.useState(null)
    const [load, setLoad] = useState(false)
    const info = {
        modules: modules, 
        group: props.location.state.group,
    }
    const group_id = props.location.state.studygroup_id

    useEffect(()=>{
        if (!load){
            fetch("http://127.0.0.1:8000/api/GetGroupModules/", {
                method: "POST",
                headers: {
                    'Accept':'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    studygroup_id: group_id
                })
            })
            .then(response => {
                return response.json()
            })
            .then(data =>{
                setLoad(true)
                setModules(data)
            })
        }
    },[load]) 

    console.log(info)
    return(
        <div className={styles.mainContainer}>
            <div className={styles.container}>
                <div className={styles.leftPanel}>
                    <StudyGroupLeft {...info}/>
                </div>
                <div className={styles.middlePanel}>
                    <StudyGroupMiddle {...info}/>
                </div>
                <div className={styles.rightPanel}>
                    <StudyGroupRight {...info}/>
                </div>
            </div>
        </div>
    )
}

export default StudyGroupHome;