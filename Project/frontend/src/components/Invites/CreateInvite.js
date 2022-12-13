import React, { useState, useEffect } from 'react';
import GetHosted from "./Components/Query/GetHosted"
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import Dropdown from 'react-bootstrap/Dropdown';
import Alert from 'react-bootstrap/Alert';
import styles from "./css/createinvite.module.css"
const CreateInvite = () => {
    const groups = GetHosted()
    const [group, setGroup] = useState('');
    const [message, setMessage] = useState(null);
    const handleSubmit = (event) => {
        event.preventDefault()
        const data = new FormData(event.currentTarget);

        fetch("http://127.0.0.1:8000/api/CreateInvite/", {
            method: "POST",
            headers: {
                'Accept':'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                token: localStorage.getItem('token'),
                studygroup_id: group,
                email: data.get('email')
            })
        })
        .then(response => {
            return response.json()
        })
        .then(data =>{
            if(data.Message != null){
                setMessage(data.Message)
            }
        })
    }

    return (
        <div>
            {
            message != null ? 
                <Alert variant = "secondary" className={styles.message}>{message}</Alert>
            : null
            }
        <Form onSubmit={handleSubmit} className={styles.container}>
            <div className={styles.header}>
                <p className={styles.headerText}>Create an invite</p>
            </div>
                <Form.Select
                    onChange = { e=> {
                        console.log("e.target.value", e.target.value);
                        setGroup(e.target.value)
                    }}
                    className={styles.drop}
                >
                {
                    groups != null ?
                        groups.Message == null ?
                            Object.entries(groups).map(([id,group]) =>{
                                return(
                                    <option 
                                    value={group.studygroup_id}
                                    name={group.studygroup_name}
                                    id={id}
                                    > {`${group.studygroup_name}`} 
                                    </option>
                                )
                            })
                        : 
                        <div className=''>
                            <Alert variant='dark'>{`${groups.Message}`}</Alert>
                        </div>
                    :null
                }
                </Form.Select>
                <Form.Control
                    type="text"
                    placeholder="Person to invite email"
                    id="email"
                    name="email"
                    autoComplete="email"
                    className={styles.drop}
                />
                <a className={styles.footer}/>
            <Button type="submit" className={styles.button}>
                Send Invite
            </Button>
        </Form>
        </div>
    )
}
export default CreateInvite;