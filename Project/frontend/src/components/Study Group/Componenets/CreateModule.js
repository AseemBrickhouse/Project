import React, { Component, useEffect, useState, ChangeEvent } from 'react';
import Button from "react-bootstrap/Button";
import {Link} from "react-router-dom";
import Form from 'react-bootstrap/Form';
import styles from "./css/CreateMaterial.module.css";
import axios from 'axios';

const CreateModule = (props) => {
    console.log(props)

    const [new_module, setModule] = useState(null);
    const [file, setFile] = useState("");
    const [group, setGroup] = useState(null);
    const [load, setLoad] = useState(false);
    const [type, setType] = useState('QUIZ');
    const [description, setDescription] = useState('default');

    useEffect(() => {
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
            setModule(data.module)
            console.log(data)
            setLoad(true)
        })
    },[])

    console.log(new_module)

    useEffect(()=>{
        if(load && new_module != null){
            fetch("http://127.0.0.1:8000/api/GetModule/", {
                method: "POST",
                headers: {
                    'Accept':'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    module_id: new_module.module_id,
                })
            })
            .then(response => {
                return response.json()
            })
            .then(data =>{
                setGroup(data)
                setLoad(false)
            })
        }   
    },[load]) 

    const handledelete = (material) => {
        console.log(material)
        fetch("http://127.0.0.1:8000/api/DeleteMaterial/", {
            method: "DELETE",
            headers: {
                'Accept':'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                module_id: material.material_id,
            })
        })
        .then(response => {
            return response.json()
        })
        .then(data =>{
            setLoad(true)
        })
    }

    const handleSubmit = (event) => {
        event.preventDefault()
        let formData = new FormData();
        formData.append('token', localStorage.getItem('token'))
        formData.append('module_id', new_module.module_id)
        formData.append('type', type)
        formData.append('content', description)
        formData.append('file', file, file.name)
        let endpoint = 'http://127.0.0.1:8000/api/CreateMaterial/'
        axios.post(endpoint, formData, {
            headers: {
                'content-type': 'multipart/form-data'
            }
        })
        .then(response =>{
            console.log(response.data)
        })
        .then(data => {
            setGroup(data) 
            setLoad(true)
        })
    }
    return(
        <div className={styles.divContainer}>   
            <Form onSubmit={handleSubmit} className={styles.form}>
                <Form.Select
                    className={styles.select}
                    label="Type"
                    onChange = { event => {
                        setType(event.target.value)
                    }}
                >
                    <option
                        value="QUIZ"
                        name="QUIZ"
                        id="QUIZ"
                        className={styles.selectOption}
                    >Quiz</option>
                    <option
                        value="STUDYGUIDE"
                        name="STUDYGUIDE"
                        id="STUDYGUIDE"
                        className={styles.selectOption}
                    >Studyguide</option>
                    <option
                        value="EXAM"
                        name="EXAM"
                        id="EXAM"
                        className={styles.selectOption}
                    >Exam</option>
                    <option
                        value="HOMEWORK"
                        name="HOMEWORK"
                        id="HOMEWORK"
                        className={styles.selectOption}
                    >Homework</option>
                </Form.Select>
                <Form.Control 
                    as="textarea" 
                    aria-label="With textarea" 
                    id="description"
                    name="description"
                    label="Description of assignment"
                    className={styles.description}
                    onChange = { event => {
                        setDescription(event.target.value)
                    }}
                />
                <Form.Control
                    type="file"
                    onChange={ event =>{
                        setFile(event.target.files[0]);
                    }}
                />
                <Button type="submit" className={styles.submit}>
                    Create Material
                </Button>
            </Form>
            <div className={styles.contentContainer}>
                {
                    group != null && group.content?
                    Object.entries(group.content).map(([_, material])=>{
                        return(
                            <div className={styles.content}>
                                {console.log(material)}
                                <div className={styles.contentLeft}>
                                    {`${material.content}`}
                                </div>
                                <div className={styles.contentMiddle}>
                                    {`${material.material_type}`}
                                </div>
                                <div className={styles.contentRight}>
                                    <Button className={styles.delete} onClick={()=>handledelete(material)}> Delete </Button>
                                </div>
                            </div>
                        )
                    })
                    :null
                }
            </div>
        </div>  
    )
}

export default CreateModule;