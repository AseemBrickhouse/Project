import React from 'react';
import {Form, FormControl } from 'react-bootstrap';

import styles from "./Componenets/css/createStudyGroup.module.css";

const CreateStudyGroup = (props) => {

    const handleSubmit = (event) => {
        event.preventDefault()
        const data = new FormData(event.currentTarget);
  
        fetch("api/CreateStudyGroup/" , {
            method: "POST",
            headers:{
              'Accept':'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                token: localStorage.getItem('token'),
                studygroup_name: data.get('Studygroupname'),
                invite_only: data.get('InviteOnly') == "Open" ? "False" : "True",
                studygroup_description: data.get('Studygroupdescription'),
            })
          })
          .then(response => {return response.json()})
          .then(data => {
            console.log(data)
          })
    }

    return (
        // <body>  
            <div className={styles.container}>
                <div className={styles.infoBox}>
                    <h1 className={styles.center}>Create Study Group</h1>
                    <div className={styles.info}>
                        <div className={styles.p}>Study Group Name:</div>
                        <div className={styles.elements}>
                            <Form onSubmit={handleSubmit}>
                            <FormControl
                                type="text"
                                placeholder="Study Group Name"
                                id="Studygroupname"
                                name="Studygroupname"
                                autoComplete="Studygroupname"
                            />
                            {['radio'].map((type) => (
                            <div key={`inline-${type}`} className={styles.inviteBox}>
                            <p className={styles.p}>Invite Only:</p>
                              <Form.Check
                                inline
                                label="Open"
                                name="InviteOnly"
                                value="Open"
                                type={type}
                                id={`inline-${type}-1`}
                                className={styles.label}
                              />
                              <Form.Check
                                inline
                                label="Closed"
                                name="InviteOnly"
                                type={type}
                                value="Closed"
                                id={`inline-${type}-2`}
                                className={styles.label}
                              />
                            </div>
                            ))}
                            <div className={styles.elements}>
                                <p className={styles.p}>Study Group Description</p>
                                <Form.Control 
                                    as="textarea" 
                                    aria-label="With textarea" 
                                    id="Studygroupdescription"
                                    name="Studygroupdescription"
                                />
                            </div>
                            <div className={styles.elements}>
             					<button className={styles.button} type="submit">Create</button>
             				</div>
                          </Form>
                        </div>
                    </div>
                </div>
            </div>
        // </body>
    );
}

export default CreateStudyGroup;

        // <body>
        // 	<div class="container">
        // 		<div class="info-box">
        // 			<h1 class="center">Create Study Group</h1>
        // 			<div class="info">
        // 				<p>Study Group Name:</p>

        // 				<div class="elements">
        // 					<input type="text" id="name" name="name" required minlength="4" maxlength="8" size="73"/>
        // 				</div>

        // 				<div class="elements">
        // 					<p>Invite Only:</p>
        // 					{/* <input type="radio" name="invite" value="Open"> Open</input>
        // 					<input type="radio" name="invite" value="Invite Only"> Invite Only</input> */}
        // 				</div>
        // 				<div class="elements">
        // 					<p>Study Group Description:</p>
        // 					<textarea rows="10" cols="75"></textarea>
        // 				</div>

        // 				<div class="elements">
        // 					<button class="full-btn">Create</button>
        // 				</div>
        // 			</div>
        // 		</div>
        // 	</div>
        // </body>