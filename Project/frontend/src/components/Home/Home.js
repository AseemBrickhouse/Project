import React, { Component } from 'react';
import {Button} from 'react-bootstrap';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from "../../store/actions/auth";

const Home = (props) => { 
    console.log(props)
    const isAuthenticated = props.isAuthenticated
    return (
        <div>
            <h1> Home Page tmp</h1>
            <div>
                {
                    !isAuthenticated ? 
                        <Link to = "/Login">
                            <Button>
                                Login
                            </Button>
                        </Link>
                    :
                        <Link to ='/Logout'>
                            <Button>
                                Logout
                            </Button>
                        </Link>
                }
            </div>
        </div>
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
  export default withRouter(connect(mapStateToProps,mapDispatchToProps)(Home));