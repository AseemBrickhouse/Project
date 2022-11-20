import React, { Component, useEffect, useState } from 'react';
import GroupCard from './Componenets/GroupCard';
import styles from "./Componenets/css/StudyGroupHome.module.css";

const StudyGroupHome = (props) =>{
    const [data, setData] = React.useState(null)
    const [load, setLoad] = useState(false)

    useEffect(() =>{
        if(!load){
            fetch("http://127.0.0.1:8000/api/GetAllUserStudyGroups/", {
                method: "POST",
                headers: {
                    'Accept':'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    token: localStorage.getItem('token')
                })
            })
            .then(response => {
                return response.json()
            })
            .then(data =>{
                setLoad(true)
                setData(data)
            })
        }
    },[load])
    
    return(
        <div className={styles.studyGroupContainer}>
            <div className={styles.studyGroupLayout}>
                {
                    data != null ?
                        Object.entries(data).map(([_, studygroup]) => {
                            return(
                                <div className={styles.groupCardContainer}>
                                    <GroupCard {...studygroup}/>
                                </div>                        
                            )
                        })
                    : null
                }
            </div>
        </div>
    )
}

export default(StudyGroupHome)