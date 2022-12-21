import React, { Component, useState, useEffect } from 'react';
import {Link} from 'react-router-dom';
import styles from "./css/peopleLayout.module.css";
import PersonCardRequest from './Components/PersonCardRequest';

const SentRequest = (props) => {
    const [people, setPeople] = useState(null)
    useEffect(()=>{
        fetch("/api/GetAllRequestOut/",{
            method: "POST",
            headers:{
                'Accept':'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                token: localStorage.getItem('token'),
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
                    Object.entries(people).map(([_, person]) => {
                        return(
                            <div className={styles.peopleCardContainer}>
                                <PersonCardRequest {...person}/>
                            </div>
                        )
                    })
                : null
            }
            </div>
        </div>
    )
}
export default SentRequest;