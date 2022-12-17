import React, { Component, useEffect, useState } from 'react';
import styles from "../Componenets/css/moduleNamesComponent.module.css";
import Button from "react-bootstrap/Button";
import {Link} from "react-router-dom";

const StudyGroupModules = (props) =>{
    console.log(props);
    // const URL = 'http://127.0.0.1:8000';
    const modules = props.modules
    const [new_module, setNewModule] = useState();
    const [file, setFile] = useState(null)
    const handleCreate = () => {
        fetch("http://127.0.0.1:8000/api/CreateModule/", {
            method: "POST",
            headers: {
                'Accept':'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                token: localStorage.getItem('token'),
                studygroup_id: props.group.studygroup_id,
            })
        })
        .then(response => {
            return response.json()
        })
        .then(data =>{
            setNewModule(data.module)
        })
        console.log(props)
    }
  
    return(
        <div className={styles.container}>
            <Link
                style={{
                    textDecoration: "none",
                    color: "black",
                    underline: "none",
                    // marginLeft: "10%"
                    }}
                    to={{
                    pathname: '/StudyGroupHome/' + props.group.studygroup_id + '/CreateModule',
                        state: { 
                              group: new_module,
                              studygroup_id: props.group.studygroup_id,
                        },
            }}>
                <Button className={styles.create}>
                    Create
                </Button>
            </Link>
		    <div className={styles.infoBox}>
                {
                modules != null ? 
                    Object.entries(modules).map(([id, modules]) => {
                        return(
                            <div className={styles.moduleContainer}>
                                <div className={styles.header}>
		    	                	{/* <div className={styles.tittle}>{`put name here`}</div> */}
		    	                	<div className={styles.uploadDate}>{ `Uploaded By: ${modules.module_owner.first_name} ${modules.module_owner.last_name}`}</div>
		    	                </div>
		    	                <div className={styles.example}></div>
                                <div className={styles.materialGroup}>
                                    {
                                    modules.content != null ? 
                                        Object.entries(modules.content).map(([_, content]) => {
                                            return(
                                                <div className={styles.buttonContainer}>
                                                    <div className={styles.buttonContainerTextType}>{`${content.material_type}`}</div>
                                                    <div className={styles.buttonContainerTextDesc}>{`${content.content}`}</div>
                                                    <a
                                                        style={{display: "hidden", marginTop: "5px", marginBottom: "5px"}}
                                                        href={content.file_content_upload}
                                                        download={content.file_content_upload}
                                                    
                                                    >
                                                    <Button className={styles.button}>
                                                        Download
                                                    </Button>
                                                    </a>
                                                </div>
                                            )
                                        })
                                    : null
                                    }
                                </div>
                            </div>
                        )
                    })
                : null
                }
		    </div>
	    </div>
    )
}

export default StudyGroupModules;