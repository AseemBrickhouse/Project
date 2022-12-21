import React, { Component, useState, useEffect } from 'react';
import {Link} from 'react-router-dom';
import styles from "./css/peopleLayout.module.css";
import PersonCardView from './Components/PersonCardView';

const ViewRequest = (props) => {
    const [people, setPeople] = useState(null)
    const [message, setMessage] = useState(null)
    useEffect(()=>{
        fetch("/api/GetAllRequestIn/",{
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
                    people.Message == null ?
                        Object.entries(people).map(([_, person]) => {
                            return(
                                <div className={styles.peopleCardContainer}>
                                    <PersonCardView {...person}/>
                                </div>
                            )
                        })
                    : <div>{people.Message}</div>
                : null
            }
            </div>
        </div>
    )
}
export default ViewRequest;