import Nav from 'react-bootstrap/Nav'
import React, { Component } from 'react';
import {Button} from 'react-bootstrap';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from "../../store/actions/auth";
import NavDropdown from 'react-bootstrap/NavDropdown';
import Container from 'react-bootstrap/Container';

import styles from "./Componenets/css/Navbar.module.css";

const Navbar = (props) => { 
    const isAuthenticated = props.isAuthenticated
    return (
        props.location.pathname != '/Logout' && props.location.pathname != '/Login' && props.location.pathname != '/CreateAccount'?
            <div style={{backgroundColor: "#2B2827"}}>
              {
                !isAuthenticated ? 
                    <Nav inverse collapseOnSelect className={styles.colorNav}>
                        <Nav.Item>
                          <Nav.Link href="/" className={styles.colorNavItem} >Some random icon</Nav.Link>
                        </Nav.Item>
                        <Nav.Link href="/Login" className={styles.colorNavItem}>Login</Nav.Link>
                        <Nav.Link href="/CreateAccount" className={styles.colorNavItem}>Sign up</Nav.Link>
                    </Nav>
                :
                <Nav inverse collapseOnSelect  className="color-nav" sticky="top">
                  <Nav.Item>
                    <Nav.Link href="/" className={styles.colorNavItem}>Some random icon</Nav.Link>
                  </Nav.Item>
                  <Nav.Item>
                    <Nav.Link eventKey="link-1" className={styles.colorNavItem}>Meeting</Nav.Link>
                  </Nav.Item>
                  <Nav.Item>
                    <Nav.Link className={styles.colorNavItem} href="/ScholarshipInformation">Scholarships</Nav.Link>
                  </Nav.Item>
                  <NavDropdown
                    title={
                        <span className={styles.colorNavItem}>People</span>
                    }
                    id="nav-dropdown"
                  >
                    <NavDropdown.Item href="/PeopleHome/Students">Students</NavDropdown.Item>
                    <NavDropdown.Item href="/PeopleHome/Instructors">Instructors</NavDropdown.Item>
                    <NavDropdown.Item href="/PeopleHome/Tutors">Tutors</NavDropdown.Item>
                  </NavDropdown>
                  <NavDropdown
                    title={
                        <span className={styles.colorNavItem}>Study Groups</span>
                    }
                    id="nav-dropdown"
                  >
                    <NavDropdown.Item href="/AllStudyGroups">View All Group</NavDropdown.Item>
                    <NavDropdown.Item href="/EnrolledStudyGroups">View Enrolled Group</NavDropdown.Item>
                    <NavDropdown.Item href="/HostedStudyGroups">View Hosted Group</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="/CreateStudyGroup">Create Group</NavDropdown.Item>
                  </NavDropdown>
                  <NavDropdown
                      title={
                          <span className={styles.colorNavItem}>Profile</span>
                      }
                      id="nav-dropdown"
                  >
                      <NavDropdown.Item href="/ViewProfile">View Profile</NavDropdown.Item>
                      <NavDropdown.Item href="/EditProfile">Edit Profile</NavDropdown.Item>
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