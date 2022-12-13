import React from 'react';
import GetInvites from './Components/Query/GetInvites';
import InviteCard from './Components/InviteCard';
import styles from "./css/invitecardLayout.module.css"
import Alert from 'react-bootstrap/Alert';

const ViewInvites = (props) => {
    console.log(props)
    const invites  = GetInvites()
    console.log(invites)
    return (
        <div className={styles.inviteContainer}>
            <div className={styles.inviteLayout}>
            {
                
                invites != null ?
                    invites.Message == null ?
                    Object.entries(invites).map(([id,invite]) => {
                        return (
                            <div className={styles.invitecardContainer}>
                                <InviteCard {...invite}/>
                            </div>
                        )
                    })
                    :                
                    <div className={styles.message}>
                        <Alert variant='dark'>{`${invites.Message}`}</Alert>
                    </div>
                : null
            }
            </div>
        </div>
    )
}
export default ViewInvites;