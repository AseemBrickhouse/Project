import React, { Component, useEffect, useState } from 'react';
import styles from "../Componenets/css/RightPanel.module.css";
import Image from "react-bootstrap/Image";


const StudyGroupRight = (props) =>{
    const group = props.group

    const [users, setUsers] = useState(null);
    const [load, setLoad] = useState(false);

    useEffect(()=>{
        if (!load){
            fetch("http://127.0.0.1:8000/api/GetUsersInGroup/", {
                method: "POST",
                headers: {
                    'Accept':'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    studygroup_id: group.studygroup_id
                })
            })
            .then(response => {
                return response.json()
            })
            .then(data =>{
                setLoad(true)
                setUsers(data)
            })
        }
    },[load]) 

    return(
        // <body>
            <div className={styles.container}>
                <div className={styles.infoBox}>
                    <div className={styles.tittle}>{`Users in ${group.studygroup_name}`}</div>
                    <div className={styles.example}></div>
                    <div className={styles.userBox}>
                    {
                        users != null ?
                            Object.entries(users).map(([_, info]) => {
                                return(
                                    <div className={styles.user}>
                                        {
                                            info.profile_pic != null ?
                                            <div className={styles.imageCropper}>
                                            <Image
                                                src={info.profile_pic}
                                                roundedCircle
                                                width={40}
                                                height={40}
                                                // style={{marginRight: "10px"}}
                                            />
                                            </div>
                                            :
                                            <div className={styles.imageCropper}>
                                            <Image
                                                src="https://cdn-icons-png.flaticon.com/512/2102/2102647.png"
                                                roundedCircle
                                                width={40}
                                                height={40}
                                                // style={{marginRight: "10px"}}
                                            />
                                            </div>
                                        }
                                        <div style={{marginLeft: "3%"}}>
                                            {`${info.first_name} ${info.last_name}`}
                                        </div>
                                    </div>
                                )
                            })
                        : null
                    }
                    </div>
                </div>
            </div>
        // </body>
    )
}

export default StudyGroupRight;