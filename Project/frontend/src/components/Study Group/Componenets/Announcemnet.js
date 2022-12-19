import React, { Component, useEffect, useState } from 'react';
import styles from "./css/Announcement.module.css";
import Form from 'react-bootstrap/Form';
import Button from "react-bootstrap/Button";
import { connect } from 'react-redux';

const Announcements = (props) =>{
    const [announcements, setAnnouncements] = useState(null)
    const [load, setLoad] = useState(true)
    useEffect(() => {
        load ?
            fetch("/api/GetGroupAnnouncements/" , {
                method: "POST",
                headers:{
                  'Accept':'application/json',
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    studygroup_id: props.group.studygroup_id,
                })
              })
              .then(response => {return response.json()})
              .then(data => {setAnnouncements(data)
                 setLoad(false)})
        : null
    },[load])

    const handleSubmit = (event) => {
        event.preventDefault()
        const data = new FormData(event.currentTarget);
        fetch("/api/CreateAnnouncement/" , {
            method: "POST",
            headers:{
              'Accept':'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                token: localStorage.getItem('token'),
                studygroup_id: props.group.studygroup_id,
                announcement_description: data.get('description')
            })
          })
          .then(response => {return response.json()})
          .then(data => {setLoad(true)})
    }
    
    const handleDelete = (announcement) => {
        fetch("/api/DeleteAnnouncement/" , {
            method: "DELETE",
            headers:{
              'Accept':'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                token: localStorage.getItem('token'),
                announcement_id: announcement.announcement_id,
            })
          })
          .then(response => {return response.json()})
          .then(data => {setLoad(true)})
    }
    return(
        <div className={styles.divContainer}>
            {
                props.account.key == props.group.studygroup_host.key ?
                <div className={styles.formContainer}>
                <div className={styles.formTitle}>Create Announcement</div>
                    <Form onSubmit={handleSubmit} className={styles.form}>
                        <Form.Control 
                            as="textarea" 
                            aria-label="With textarea" 
                            id="description"
                            name="description"
                            label="description"
                            className={styles.description}
                        />
                        <Button type="submit" className={styles.submit}>
                            Create Announcement
                        </Button>
                    </Form>
                </div>
                : null

            }
            <div className={styles.contentContainer}>
                <div className={styles.formTitle}>Current Announcements</div>
                {
                    announcements != null ? 
                        Object.entries(announcements).map(([_,announcement])=>{
                            return(
                                <div className={styles.content}>
                                    <div className={styles.contentLeft}>{`${announcement.announcement_creator.first_name} ${announcement.announcement_creator.last_name}`}</div>
                                    <div className={styles.contentMiddle}>{`${announcement.announcement_description}`}</div>
                                    {
                                        props.account.key == props.group.studygroup_host.key ?
                                        <div className={styles.contentRight}><Button className={styles.delete} onClick={()=>{handleDelete(announcement)}}>Delete</Button></div>
                                        :null
                                    }
                                </div>
                            )
                        })
                    :  null
                }
            </div>
        </div>
    )
}

const mapStateToProps = (state) =>{
    return{
        account: state.auth.account,
    }
}
export default connect(mapStateToProps, null)(Announcements);