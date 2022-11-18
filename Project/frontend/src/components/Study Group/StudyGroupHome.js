import React, { Component, useEffect, useState } from 'react';
import {Button} from 'react-bootstrap';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import GroupCard from './Componenets/GroupCard';

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
        <div>
            {
                data != null ?
                    Object.entries(data).map(([studygroup_id, studygroup]) => {
                        return(
                            <div>
                                <GroupCard {...studygroup}/>
                            </div>                        
                        )
                    })
                : null
            }
        </div>
    )
}

export default(StudyGroupHome)