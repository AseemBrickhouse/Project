import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";
import Home from './Home/Home';
import Login from '../components/Login/Login';
import Logout from '../components/Login/Logout';
import CreateAccount from '../components/SignUp/CreateAccount';
import AccountCreated from '../components/SignUp/AccountCreated';
import RecoveryMessage from '../components/Login/RecoveryMessage';
import RecoveryPassword from './Login/RecoveryPassword';
import Navbar from './Navbar/Navbar';
import ScholarShipInformation from './Scholarship/ScholarshipInformation';
import CreateStudyGroup from './Study Group/CreateStudyGroup';
import EnrolledStudyGroups from './Study Group/EnrolledStudyGroups';
import AllStudyGroups from './Study Group/AllStudyGroups';
import StudyGroupHome from './Study Group/StudyGroupHome';
import StudyGroupsHosted from './Study Group/StudyGroupsHosted';
import ViewProfile from './People/Profile/ViewProfile';
import EditProfile from './People/Profile/EditProfile';
import PeopleHome from './People/PeopleHome';
import PeopleStudents from './People/PeopleStudents';
import PeopleTutors from './People/PeopleTutors';
import PeopleInstructors from './People/PeopleInstructors';
import ViewInvites from './Invites/ViewInvites';
import CreateInvite from './Invites/CreateInvite';
import CreateModule
 from './Study Group/Componenets/CreateModule';
const Routes = (props) => {
    return (
        <React.Fragment>
            <Router>
                <Navbar {...props}/>
                <Switch>
                    <Route exact path = "/"><Home/></Route>

                    {/* /Login */}
                    <Route exact path = "/Login" component={Login}/>
                    <Route exact path = "/Logout" component={Logout}/>
                    <Route exact path = "/AccountCreated" component={AccountCreated}/>
                    <Route exact path = "/RecoveryMessage" component={RecoveryMessage}/>
                    <Route exact path = "/RecoveryPassword" component={RecoveryPassword}/>

                    {/* /SignUp */}
                    <Route exact path = "/AccountCreated" component={AccountCreated}/>
                    <Route exact path = "/CreateAccount" component={CreateAccount}/>

                    {/* Studygroup */}
                    <Route exact path = "/AllStudyGroups" component={AllStudyGroups}/>
                    <Route exact path = "/EnrolledStudyGroups" component={EnrolledStudyGroups}/>
                    <Route exact path = "/HostedStudyGroups" component={StudyGroupsHosted}/>
                    <Route exact path = "/CreateStudyGroup" component={CreateStudyGroup}/>
                    <Route exact path = {'/StudyGroupHome/:id'} component={StudyGroupHome}/>
                    {/* <Route exact path = "/CreateModule" component={CreateModule}/> */}

                    {/* Scholarship */}
                    <Route exact path = "/ScholarshipInformation" component={ScholarShipInformation}/>

                    {/* Profile */}
                    <Route exact path = "/ViewProfile" component={ViewProfile}/>
                    <Route exact path = {'/ViewProfile/:key'}>
                        <ViewProfile {...props}/>
                    </Route>
                    <Route exact path = "/EditProfile" component={EditProfile}/>

                    {/* Invite */}
                    <Route exact path = "/CreateInvite" component={CreateInvite}/>
                    <Route exact path = "/ViewInvite" component={ViewInvites}/>
                    <Route exact path = {'/ViewInvite/:key'}>
                        <ViewInvites {...props}/>
                    </Route>

                    {/* People */}
                    <Route exact path = "/PeopleHome" component={PeopleHome}/>
                    <Route exact path = "/PeopleHome/Students" component={PeopleStudents}/>
                    <Route exact path = "/PeopleHome/Instructors" component={PeopleInstructors}/>
                    <Route exact path = "/PeopleHome/Tutors" component={PeopleTutors}/>

                    <Route exact path = "/test" component={CreateModule}/>


                </Switch>
            </Router>
        </React.Fragment>
    )
}

export default Routes;