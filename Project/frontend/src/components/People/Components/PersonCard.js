import React, { Component, useState, useEffect } from 'react';
import {Link} from 'react-router-dom';
import styles from "../css/people.module.css";
import { Image } from 'react-bootstrap';
import { Button } from 'react-bootstrap';
const PersonCard = (props) => {
    const [person, setPerson] = useState(props);
    const [load, setLoad] = useState(false)
    useEffect(() => {
        !load ?
            fetch("/api/GetPerson/",{
                method: "POST",
                headers:{
                    'Accept':'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    token: localStorage.getItem('token'),
                    first_name: props.first_name,
                    last_name: props.last_name,
                    email: props.email,
                })
            })
            .then(response => {
                return response.json();
            })
            .then(data=>{
                setPerson(data)
                setLoad(true)
            })
        : null
    },[load])
    console.log(person)
    const handleAdd = (person) => {
        fetch("/api/SendFriendRequest/",{
            method: "POST",
            headers:{
                'Accept':'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                token: localStorage.getItem('token'),
                key: person.key,
            })
        })
        .then(response => {
            return response.json();
        })
        .then(data=>{
            setPerson(data)
            setLoad(false)
        })
    }
    const handleRemove = (person) => {

    }
    return(
    <div className={styles.container}>
        <div className={styles.infoBox}>
            <div className={styles.cardHeader}>
                <div>
                {
                person.profile_pic != null ?
                    <Image
                        src={person.profile_pic}
                        roundedCircle
                        width={50}
                        height={50}
                        style={{marginRight: "10px", marginLeft: "10px"}}
                    />
                    :
                    <Image
                        src="https://cdn-icons-png.flaticon.com/512/2102/2102647.png"
                        roundedCircle
                        width={50}
                        height={50}
                        style={{marginRight: "10px", marginLeft: "10px"}}
                    />
                }
                </div>
                <div className={styles.cardHeaderName}>
                    {`${person.first_name} ${person.last_name}`}
                </div>
            </div>
            <div className={styles.cardBody}>
                {person.phone != null ?
                    <div className={styles.subBody}>
                        <p className={styles.heading}>{`Phone number: `}</p>
                        <p className={styles.cardBodyText}>{`${person.phone}`}</p>
                    </div>
                    :
                    <div className={styles.subBody}>
                        <p className={styles.heading}>{`Phone number: `}</p>
                        <p className={styles.cardBodyText}>{`NA`}</p>
                    </div>
                    }
                <div className={styles.subBody}>
                    <p className={styles.heading}>{`Role: `}</p>
                    <p className={styles.cardBodyText}>{`${person.role}`}</p>
                </div>
                <div className={styles.subBody}>
                    <p className={styles.heading}>{`Bio: `}</p>
                    <p className={styles.cardBodyText}>{`${person.bio}`}</p>
                </div>
            </div>
            <div className={styles.cardFooter}>
            <Link
			    style={{
			    textDecoration: "none",
			    color: "black",
			    underline: "none",
			    marginLeft: "10%"
			    }}
			    to={{
			    pathname: '/ViewProfile/' + person.key + '/',
			    	state: { 
			      		person_key: person.key,
			      		person: person,
			    	},
			    }}>
			    <div className={styles.newb} style={{backgroundColor: "#A7916D", marginLeft:"-50%", transform: "translateX(25%)"}}>View Profile</div>
			    </Link>
                {
                    person.is_friend == "True" ? 
                    <div style={{backgroundColor: "#A04848", borderRadius: "5px"}}>
                        <Button className={styles.newb} onClick={()=>handleRemove(person)}>
                            Remove
                        </Button>
                    </div>
                    : person.is_friend == "Waiting"?
                    <div style={{backgroundColor: "#A04848", borderRadius: "5px"}}>
                        <Button className={styles.newb}>
                            Waiting
                        </Button>
                    </div>
                    :
                    <div style={{backgroundColor: "#A04848", borderRadius: "5px"}}>
                        <Button className={styles.newb} onClick={()=>handleAdd(person)}>
                            Add Friend
                        </Button>
                    </div>
                }
            </div>
        </div>
    </div>
    )
}
export default PersonCard;