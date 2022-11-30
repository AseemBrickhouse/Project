import React, { Component, useEffect, useState } from 'react';
import styles from "../Componenets/css/moduleNamesComponent.module.css";

const StudyGroupModules = (props) =>{

    const modules = props.modules

    return(
        <div className={styles.container}>
		    <div className={styles.infoBox}>
                {
                modules != null ? 
                    Object.entries(modules).map(([id, modules]) => {
                        return(
                            <div>
                                <div className={styles.header}>
		    	                	<div className={styles.tittle}>{`put name here`}</div>
		    	                	<div className={styles.uploadDate}>{ `Uploaded By: ${modules.module_owner.first_name} ${modules.module_owner.last_name}`}</div>
		    	                </div>
		    	                <div className={styles.example}></div>
                                <div className={styles.materialGroup}>
                                    {
                                    modules.content != null ? 
                                        Object.entries(modules.content).map(([_, content]) => {
                                            return(
                                                <div>
                                                    <button className={styles.button}>
                                                        {`${content.material_type}  ${content.content}`}
                                                    </button>
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