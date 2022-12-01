import React, { Component, useEffect, useState, useRef } from 'react';
import styles from "./Css/NewChat.module.css";
import Image from "react-bootstrap/Image";
import Message from './Componenets/Message';
import {PlusCircleFill} from "react-bootstrap-icons";
import {ArrowReturnRight} from "react-bootstrap-icons";
import Form from 'react-bootstrap/Form';

const ChatRoom = (props) =>{
    console.log(props)
    const group = props.group
    const reload = true
    const [messages, setMessages] = useState(null);
    const [load, setLoad] = useState(true);
    const bottomRef = useRef(null);



    
    useEffect(() => {
        if(props != null){
            bottomRef.current.scrollIntoView({behavior: 'smooth'});

        }
      }, [messages]);

    useEffect(()=>{
        if (load){
            fetch("http://127.0.0.1:8000/api/GetAllMessages/", {
                method: "POST",
                headers: {
                    'Accept':'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    studygroup_id: group.studygroup_id
                })
            })
            .then(response => {
                return response.json()
            })
            .then(data =>{
                setLoad(false)
                console.log(data)
                setMessages(data)
            })
        }
    },[load])

    if(!load && reload){
        setTimeout(() => setLoad(true), 5000)
    }
    const handleCreation = (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);
        console.log(data.get('message'))
        fetch("http://127.0.0.1:8000/api/CreateMessage/", {
            method: "POST",
            headers: {
                'Accept':'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                token: localStorage.getItem('token'),
                message:data.get('message'),
                studygroup_id: group.studygroup_id,
            })
        })
        .then(response => {
            return response.json()
        })
        .then(data =>{
            setLoad(true)
        })
        
    }
    return(
        <div className={styles.mainChatContainer}>
            <div className={styles.chatRoomBody}>
                {
                    messages != null ? 
                        Object.entries(messages).map(([id, message]) =>{
                            return(
                                <Message {...message}/>
                            )
                        })
                    : null
                    
                }
            <div ref={bottomRef} />
            </div>
            <div className={styles.chatRoomFooter}>
                <Form className={styles.chatRoomFooterTextBox} onSubmit={handleCreation}>
                    <Form.Control
                        className={styles.chatRoomFooterInput}
                        id="message"
                        type="text"
                        name="message" 
                        placeholder="Message chat"
                    />
                </Form> 
            </div>
        </div>
    )
}

export default ChatRoom;

{/* <Image
src="https://cdn-icons-png.flaticon.com/512/2102/2102647.png"
roundedCircle
width={50}
height={50}
style={{marginRight: "10px"}}
/> */}

{/* <section classNameName={styles.chatbox}>
<section className={styles.chatWindow}>
    <article className="msg-container msg-self" id="msg-0">
        <div className={styles.msgBox}>
            <div className={styles.flr}>
                <div className={styles.messages}>
                    <p className={styles.msg} id="msg-1">
                        Lorem ipsum dolor sit amet
                    </p>
                    <p className={styles.msg} id="msg-2">
                        Praesent varius
                    </p>
                </div>
                <span className={styles.timestamp}><span className={styles.username}>Name</span>&bull;<span className="posttime">2 minutes ago</span></span>
            </div>
            <img className={styles.userImg} id="user-0" src="//gravatar.com/avatar/56234674574535734573000000000001?d=retro" />
        </div>
    </article>
    <article className={styles.msgContainer} id="msg-0">
        <div className={styles.msgBox}>
            <img className={styles.userImg} id="user-0" src="//gravatar.com/avatar/00034587632094500000000000000000?d=retro" />
            <div className={styles.flr}>
                <div className={styles.messages}>
                    <p className={styles.msg} id="msg-0">
                        Lorem ipsum dolor sit amet.
                    </p>
                </div>
                <span className={styles.timestamp}><span className={styles.username}>Name</span>&bull;<span className={styles.posttime}>Now</span></span>
            </div>
        </div>
    </article>
</section>
<form className={styles.chatInput} onsubmit="return false;">
    <input type={styles.text} autocomplete="on" placeholder="Type a message" />
    <button>
        <svg style={{width: "24px", height: "24px"}} viewBox="0 0 24 24"><path fill="rgba(0,0,0,.38)" d="M17,12L12,17V14H8V10H12V7L17,12M21,16.5C21,16.88 20.79,17.21 20.47,17.38L12.57,21.82C12.41,21.94 12.21,22 12,22C11.79,22 11.59,21.94 11.43,21.82L3.53,17.38C3.21,17.21 3,16.88 3,16.5V7.5C3,7.12 3.21,6.79 3.53,6.62L11.43,2.18C11.59,2.06 11.79,2 12,2C12.21,2 12.41,2.06 12.57,2.18L20.47,6.62C20.79,6.79 21,7.12 21,7.5V16.5M12,4.15L5,8.09V15.91L12,19.85L19,15.91V8.09L12,4.15Z" /></svg>
    </button>
    {/* <button>
            <svg style={{width: "24px", height: "24px"}} viewBox="0 0 24 24"><path fill="rgba(0,0,0,.38)" d="M17,12L12,17V14H8V10H12V7L17,12M21,16.5C21,16.88 20.79,17.21 20.47,17.38L12.57,21.82C12.41,21.94 12.21,22 12,22C11.79,22 11.59,21.94 11.43,21.82L3.53,17.38C3.21,17.21 3,16.88 3,16.5V7.5C3,7.12 3.21,6.79 3.53,6.62L11.43,2.18C11.59,2.06 11.79,2 12,2C12.21,2 12.41,2.06 12.57,2.18L20.47,6.62C20.79,6.79 21,7.12 21,7.5V16.5M12,4.15L5,8.09V15.91L12,19.85L19,15.91V8.09L12,4.15Z" /></svg>
    </button> */}
// </form>
// </section> */}