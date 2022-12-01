import React, { Component, useState, useEffect } from 'react';
import {Link} from 'react-router-dom';
import styles from "./css/peopleLayout.module.css";
import PersonCard from './Components/PersonCard';

const PeopleStudents = (props) => {
    const [people, setPeople] = useState(null)
    useEffect(()=>{
        fetch("/api/GetPeopleRole/",{
            method: "POST",
            headers:{
                'Accept':'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                token: localStorage.getItem('token'),
                role: "STUDENT",
            })
        })
        .then(response=> {
            return response.json();
        })
        .then(data=>{
            setPeople(data)
        })
    },[])
    console.log(people)
    return(
        <div className={styles.peopleContainer}>
            <div className={styles.peopleLayout}>
            {
                people != null ?
                    Object.entries(people).map(([key, person]) => {
                        return(
                            <div className={styles.peopleCardContainer}>
                                {console.log(person)}
                                <PersonCard {...person}/>
                            </div>
                        )
                    })
                : null
            }
            </div>
        </div>
    )
}
export default PeopleStudents;