import React, { useState } from 'react';
import styles from "../css/invitecard.module.css"
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

const InviteCard = (props) => {
    const [accept, setAccept] = useState(false)
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

    const handleDecline = (id) => {
        fetch("api/DeleteInvite/", {  
			method: "POST",
			headers:{
				'Accept':'application/json',
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				token: localStorage.getItem('token'),
				invite_id: id,
			})
		})
		.then(response=>{
			return response.json()
		})
    }
    const handleAccept = (studygroup_id) => {
		fetch("api/JoinStudyGroup/", {  
			method: "POST",
			headers:{
				'Accept':'application/json',
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				token: localStorage.getItem('token'),
				studygroup_id: studygroup_id,
			})
		})
		.then(response=>{
			return response.json()
		})
        setAccept(!accept)
    }
    const studygroup = props.studygroup_info
    const sender = props.sender
    const recipient = props.recipient
    const expiration_date_date = new Date(props.expiration_date).getMonth() % 12 + '/' + new Date(props.expiration_date).getDate() + '/' + new Date(props.expiration_date).getFullYear();
    const expiration_date_time = formatDate(props.expiration_date)

    return (
        <Card style={{ width: '18rem', backgroundColor: "#2B2827" }}>
          <Card.Body style={{ backgroundColor: "#2B2827" }}>
            <Card.Title style={{color: "white"}}>{`Group: ${studygroup.studygroup_name}`}</Card.Title>
            <Card.Subtitle className="mb-2 text-muted" style={{color: "white"}}>{`Invite`}</Card.Subtitle>
            <Card.Text style={{color: "white"}}>{`Expiration date: ${expiration_date_date} at ${expiration_date_time}`}</Card.Text>
            <Card.Link>
                <Button className={styles.buttonDecline} onClick={() => {handleDecline(props.invite_id)}}>
                    Decline
                </Button>
            </Card.Link>
            <Card.Link>
                {
                    !accept ?
                    <Button onClick={() => {handleAccept(studygroup.studygroup_id)}} className={styles.buttonAccept}>
                        Accept
                    </Button>
                :                
                    <Button className={styles.buttonAccepted} style={{backgroundColor: "#249761"}}>
                        Accepted
                    </Button>
                }
            </Card.Link>
          </Card.Body>
        </Card>
    )
}
export default InviteCard;