import React, { Component, useEffect, useState } from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";
import StudyGroupNav from './StudyGroupNav';
import StudyGroupModules from './StudyGroupModules';


const StudyGroupMiddle = (props) =>{
    const group = props

    return(
        <React.Fragment>
            <Router>
                <StudyGroupNav/>
                <Switch>
                    <StudyGroupModules {...props}/>
                </Switch>
            </Router>
        </React.Fragment>
    )
}

export default StudyGroupMiddle;