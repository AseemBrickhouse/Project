import React, { Component, useEffect, useState } from 'react';
import styles from "../Css/NewChat.module.css";
import Image from "react-bootstrap/Image";

const Message = (props) => {
    const message = props
    const creation_date = new Date(message.creation_date)
    let date = creation_date.toLocaleDateString() + creation_date.toLocaleTimeString();
    return(
        <div className={styles.chatRoomMsgContainer}>
        {
            message.account.profile_pic != null ?
            <Image
                src={message.account.profile_pic}
                roundedCircle
                width={40}
                height={40}
                style={{marginRight: "10px", marginLeft: "10px"}}
            />
            :
            <Image
                src="https://cdn-icons-png.flaticon.com/512/2102/2102647.png"
                roundedCircle
                width={40}
                height={40}
                style={{marginRight: "10px", marginLeft: "10px"}}
            />
        }
            <div className={styles.chatRoomMsg}>
                <div className={styles.chatRoomMsgHeader}>
                    <div className={styles.chatRoomMsgUsername}>
                    {`${message.account.first_name} ${message.account.last_name}`}
                    </div>
                    <div className={styles.chatRoomMsgTime}>
                        {`${date}`}
                    </div>
                </div>
                <div className={styles.chatRoomMsgContent}>
                    {`${message.content}`}
                </div>
            </div>
        </div>
    )
}

export default Message;