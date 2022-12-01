import React, { Component } from 'react';
import {Image, Form, FormControl} from 'react-bootstrap';
import styles from '../css/profile.module.css';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';

class EditProfile extends Component{
    constructor(props){
        super(props);
        this.state = {
            first_name: "",
            last_name: "",
            account_role: "",
            phone: "",
            bio: "",
            email: "",
            profile_pic: null,
        };
    }
    componentDidMount(){
        fetch("http://127.0.0.1:8000/api/CurrentUser/", {
            method:"POST",
            headers:{
              'Accept':'application/json',
              'Content-Type': 'application/json',
            },
                body: JSON.stringify({
                    token: localStorage.getItem('token')
                })
            })
            .then(response =>{
                if(response.status > 400){
                    return this.setState(() => {
                        return{ placeholder: "Something went wrong!" };
                    });
                }
                return response.json();
            })
            .then(data =>{
              return this.setState({
                first_name: data.first_name,
                last_name: data.last_name,
                account_role: data.role,
                phone: data.phone_number,
                bio: data.bio,
                email: data.email,
                profile_pic: data.profile_pic,
              })            
            });
    }

    Form = () => {
        const defaultValues = {
            first_name: this.state.first_name,
            last_name: this.state.last_name,
            phone: this.state.phone,
            bio: this.state.bio,
            email: this.state.email,
            role: this.state.role,
            profile_pic: this.state.profile_pic,
        }
        const [formValues, setFormValues] = React.useState(defaultValues);
        const handleInputChange = (event) =>{
            const {name, value} = event.target;
            console.log(name, value)
            setFormValues({
                ...formValues,
                [name]: value,
            });
        };
        const handleSubmit = (event) => {
            event.preventDefault();
            console.log(formValues);
            fetch("/api/EditAccount/" , {
                method: "PUT",
                headers:{
                    'Accept':'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    token: localStorage.getItem('token'),
                    first_name: formValues.first_name,
                    last_name: formValues.last_name,
                    phone: formValues.phone,
                    bio: formValues.bio,
                    email: formValues.email,
                    role: formValues.role,
                })
            }).then(response=>{
                console.log(response)
                // window.location.reload()
            })
        }
        return (
            <Form className={styles.container} onSubmit={handleSubmit}>
                <div className={styles.loginBox}>
                    <div className={styles.tittle}>
                        <h1 style={{color: "white"}}>User Account</h1>
                    </div>
                    {
                    defaultValues.profile_pic != null ?
                    <Image
                        src={defaultValues.profile_pic}
                        roundedCircle
                        width={200}
                        height={200}
                        style={{marginRight: "10px", marginLeft: "10px", marginBottom: "10px"}}
                    />
                    :
                    <Image
                        src="https://cdn-icons-png.flaticon.com/512/2102/2102647.png"
                        roundedCircle
                        width={200}
                        height={200}
                        style={{marginRight: "10px", marginLeft: "10px"}}
                    />
                    }
                    <div className={styles.login}>
                        <FormControl
                            className={styles.elements}
                            type="text"
                            placeholder={defaultValues.first_name == '' ? "First Name" : defaultValues.first_name}
                            name="first_name"
                            value={formValues.first_name}
                            onChange={handleInputChange}
                        />
                        <FormControl
                            className={styles.elements}
                            type="text"
                            placeholder={defaultValues.last_name == '' ? "Last Name" : defaultValues.last_name}
                            name="last_name"
                            value={formValues.last_name}
                            onChange={handleInputChange}
                        />
                        <FormControl
                            className={styles.elements}
                            type="text"
                            placeholder={defaultValues.email == '' ? "Email" : defaultValues.email}
                            name="email"
                            value={formValues.email}
                            onChange={handleInputChange}
                        />
                        <FormControl
                            className={styles.elements}
                            type="text"
                            placeholder={defaultValues.phone == '' ? "Phone Number" : defaultValues.phone}
                            name="phone"
                            value={formValues.phone}
                            onChange={handleInputChange}
                        />
                        {['radio'].map((type) => (
                            <div key={`inline-${type}`} className={styles.radio}>
                            <p className={styles.p} style={{marginRight: "10px"}}>Role:</p>
                              <Form.Check
                                inline
                                label="PROFESSOR"
                                name="role"
                                value="STUDENT"
                                type={type}
                                id={`inline-${type}-1`}
                                className={styles.label}
                                onChange={handleInputChange}

                              />
                              <Form.Check
                                inline
                                label="STUDENT"
                                name="role"
                                type={type}
                                value="STUDENT"
                                id={`inline-${type}-2`}
                                className={styles.label}
                                onChange={handleInputChange}

                              />
                                <Form.Check
                                inline
                                label="TA"
                                name="role"
                                type={type}
                                value="TA"
                                onChange={handleInputChange}

                                id={`inline-${type}-2`}
                                className={styles.label}
                              />
                            </div>
                            ))}
                        <FormControl
                            className={styles.elements}
                            style={{height: "100px", overflowWrap: "break-word"}}
                            type="text"
                            placeholder={defaultValues.bio == '' ? "Bio" : defaultValues.bio}
                            name="bio"
                            value={formValues.bio}
                            onChange={handleInputChange}
                        />
                    </div>
                    <button className={styles.button} type="submit">
                        Change
                    </button>   
                </div>
            </Form>
        )
    }
    render(){
        return(
            <this.Form/>
        )
    }
}

export default EditProfile;