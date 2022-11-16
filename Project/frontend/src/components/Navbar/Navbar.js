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
        props.location.pathname != '/Logout' &&props.location.pathname != '/Login' ?
            <div>
              {
                !isAuthenticated ? 
                    <Nav inverse collapseOnSelect>
                        <Nav.Item>
                          <Nav.Link href="/">Some random icon</Nav.Link>
                        </Nav.Item>
                        <Nav.Link href="/Login">Login</Nav.Link>
                    </Nav>
                :
                <Nav inverse collapseOnSelect className="color-nav">
                        <Nav.Item>
                          <Nav.Link href="/" className="color-nav-item">Some random icon</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                          <Nav.Link eventKey="link-1" className="color-nav-item">Meeting</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                          <Nav.Link eventKey="link-2" className="color-nav-item" >Study Groups</Nav.Link>
                        </Nav.Item>
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
                        <Nav.Link href="/Logout">Logout</Nav.Link>
                    </NavDropdown>
                </Nav>
              }
              </div>
            :<></>
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