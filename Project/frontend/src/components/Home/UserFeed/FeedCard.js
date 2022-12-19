import React, { Component, useEffect, useState } from 'react';
import {Button} from 'react-bootstrap';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import Card from 'react-bootstrap/Card';
import Image from "react-bootstrap/Image";

import styles from "./Components/Feed css/feed.modules.css";

const FeedCard = (props) =>{
    const formatDate = (date) => {
        if (date == null){
            return;
        }
        var hours = new Date(date).getHours();
        var minutes = new Date(date).getMinutes();

        var newformat = hours >= 12 ? 'PM' : 'AM';

        hours = hours % 12; 

        hours = hours ? hours : 12; 
        minutes = minutes < 10 ? '0' + minutes : minutes;

        return `${hours}:${minutes} ${newformat}`
    }
    const info = props;
    const CreationDate = new Date(info.Body.Dates.Creation_date).getMonth() % 12 + '/' + new Date(info.Body.Dates.Creation_date).getDate() + '/' + new Date(info.Body.Dates.Creation_date).getFullYear();
    let meetingDate = null
    let start = formatDate(info.Body.Dates.Start_date)
    let end = formatDate(info.Body.Dates.End_date)
    if (info.Body.Dates.Start_date != null){
        meetingDate = new Date(info.Body.Dates.Start_date).getMonth() % 12 + '/' + new Date(info.Body.Dates.Start_date).getDate() + '/' + new Date(info.Body.Dates.Start_date).getFullYear();
    }
    return(
        <div>
            <Card style={{marginBottom: "5px", height: "200px", overflowY: "hidden"}}>
                <Card.Body className={styles.Feed}>
                  <Card.Title className={styles.FeedHeader}>
                    {
                        info.Body.Users.Sender.Info.profile_pic != null ?
                        <Image
                            src={info.Body.Users.Sender.Info.profile_pic}
                            roundedCircle
                            width={50}
                            height={50}
                            style={{marginRight: "10px"}}
                        />
                        :
                        <Image
                            src="https://cdn-icons-png.flaticon.com/512/2102/2102647.png"
                            roundedCircle
                            width={50}
                            height={50}
                            style={{marginRight: "10px"}}
                        />
                    }
                    {`${info.Body.Users.Sender.Info.first_name} ${info.Body.Users.Sender.Info.last_name}`}
                </Card.Title>
                  <Card.Text className={styles.FeedText}>      
                    {info.Body.Sub_Type.Type == "Announcement" ?
                        `Announcement from group ${info.Header.Name}`
                    : null}
                    {info.Body.Sub_Type.Type == "Module/Material" ?
                        `Module/Material upload from group ${info.Header.Name}`
                    : null}
                    {info.Header.Type == "Meeting" ?
                        `Scheduled meeting on ${meetingDate}            ${start} - ${end}`
                    : null}
                    {info.Body.Sub_Type.Type != null && info.Body.Sub_Type.Type == "Invite" ?
                        `${info.Body.Users.Sender.Info.first_name} Invited you to  study group ${info.Header.Name}`
                    : null} 
                  </Card.Text>
                  <Card.Text className={styles.FeedCardDescription}>
                    {
                        info.Body.Sub_Type.Type == "Module/Material" ? 
                        <div style={{whiteSpace: "pre"}}>
                            {`${info.Body.Info.Description}`}
                        </div>
                        :
                        info.Body.Info.Description != null ?
                        <div style={{whiteSpace: "normal"}}>
                            {`${info.Body.Info.Description}`}
                        </div>
                        : null
                    }

                  </Card.Text>
                </Card.Body>
            </Card>
        </div>
    )
}

export default FeedCard;