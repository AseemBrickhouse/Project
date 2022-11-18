import Nav from 'react-bootstrap/Nav'
import React, { Component } from 'react';
import {Button} from 'react-bootstrap';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from "../../store/actions/auth";
import NavDropdown from 'react-bootstrap/NavDropdown';

const Navbar = (props) => { 
    const isAuthenticated = props.isAuthenticated
    return (
        props.location.pathname != '/Logout' && props.location.pathname != '/Login' ?
            <div>
               {/* <div class="navContainer">
                 <div class="navigation">
                     <li><a href="/">Random Icon</a></li>
                     <li><a href="/home/">Students</a></li>
                     <li><a href="/courses/">Instructors</a></li>
                     <li><a href="/users/">Tutors</a></li>
                     <li><a href="/StudyGroupHome">Studygroup</a></li>
                     <li><a href="/ScholarshipInformation">Scholarships</a></li>
                     {
                       !isAuthenticated ? 
                         <li><a href="/Login">Login</a></li>
                       : 
                       <li><a href="/Logout">Logout</a></li>
                     }
                 </div>
             </div> */}
              {
                !isAuthenticated ? 
                    <Nav inverse collapseOnSelect className="color-nav">
                        <Nav.Item>
                          <Nav.Link href="/" className="color-nav-item" >Some random icon</Nav.Link>
                        </Nav.Item>
                        <Nav.Link href="/Login" className="color-nav-item">Login</Nav.Link>
                    </Nav>
                :
                <Nav inverse collapseOnSelect  className="color-nav">
                  <Nav.Item>
                    <Nav.Link href="/" className="color-nav-item">Some random icon</Nav.Link>
                  </Nav.Item>
                  <Nav.Item>
                    <Nav.Link eventKey="link-1" className="color-nav-item">Meeting</Nav.Link>
                  </Nav.Item>
                  <Nav.Item>
                    <Nav.Link className="color-nav-item" href="/ScholarshipInformation">Scholarships</Nav.Link>
                  </Nav.Item>
                  <NavDropdown
                    title={
                        <span className="color-nav-item">People</span>
                    }
                    id="nav-dropdown"
                  >
                    <NavDropdown.Item href="/CreateStudyGroup">Students</NavDropdown.Item>
                    <NavDropdown.Item href="/CreateStudyGroup">Instructors</NavDropdown.Item>
                    <NavDropdown.Item href="/CreateStudyGroup">Tutors</NavDropdown.Item>
                  </NavDropdown>
                  <NavDropdown
                    title={
                        <span className="color-nav-item">Study Groups</span>
                    }
                    id="nav-dropdown"
                  >
                    <NavDropdown.Item href="/CreateStudyGroup">View All Group</NavDropdown.Item>
                    <NavDropdown.Item href="/CreateStudyGroup">View Enrolled Group</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="/CreateStudyGroup">Create Group</NavDropdown.Item>
                  </NavDropdown>
                  <NavDropdown
                      title={
                          <span className="color-nav-item">Profile</span>
                      }
                      id="nav-dropdown"
                  >
                      <NavDropdown.Item >View Profile</NavDropdown.Item>
                      <NavDropdown.Item >Edit Profile</NavDropdown.Item>
                      <NavDropdown.Item >View Friends</NavDropdown.Item>
                      <NavDropdown.Divider />
                      <NavDropdown.Item href="/Logout">Logout</NavDropdown.Item>
                  </NavDropdown>
                </Nav>
              }
              </div>
            : null
          );
}
const mapStateToProps = (state) => {
    return{
        isAuthenticated: state.auth.token !== null,
        account: state.auth.account
    }
  }
  const mapDispatchToProps = dispatch => {
      return {
        logout : () => dispatch(actions.authLOGOUT())
      }
  }
  export default withRouter(connect(mapStateToProps,mapDispatchToProps)(Navbar));