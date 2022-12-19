import React, { Component, useEffect, useState } from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";
import StudyGroupNav from './StudyGroupNav';
import StudyGroupModules from './StudyGroupModules';
import ChatRoom from '../../Chatroom/ChatRoom';
import CreateModule from './CreateModule';
import Announcements from './Announcemnet';
const StudyGroupMiddle = (props) =>{

    return(
        <React.Fragment>
            <Router>
                <StudyGroupNav {...props}/>
                <Switch>
                    <Route exact path = {'/StudyGroupHome/:key/Modules'}>
                        <StudyGroupModules {...props}/>
                    </Route>
                    <Route exact path = {'/StudyGroupHome/:key/ChatRoom'}>
                        <ChatRoom {...props}/>
                    </Route>
                    <Route exact path = {'/StudyGroupHome/:key/CreateModule'}>
                        <CreateModule {...props}/>
                    </Route>
                    <Route exact path = {'/StudyGroupHome/:key/Announcements'}>
                        <Announcements {...props}/>
                    </Route>
                </Switch>
            </Router>
        </React.Fragment>
    )
}

export default StudyGroupMiddle;