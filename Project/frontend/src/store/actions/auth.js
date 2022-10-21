import * as actionTypes from './types';
import axios from 'axios';


export const authSUCCESS = token =>{
    return{
        type: actionTypes.AUTH_SUCCESS,
        token: token
    };
}

export const authFAIL = (error) =>{
    return{
        type: actionTypes.AUTH_FAIL,
        error: error
    };
}

export const getAuthInfoSUCCESS = (account) =>{
    return{
        type: actionTypes.GET_AUTH_ACCOUNT,
        account: account,
    }
}

export const getAuthInfoFAIL = error =>{
    return{
        type: actionTypes.GET_AUTH_ACCOUNT,
        error: error,
    }
}
export const getAuthInfo = (token) =>{
    return dispatch=>{
        axios.post("http://127.0.0.1:8000/api/CurrentUser/", {
            // csrf: localStorage.getItem('csrftoken'),
            token: token,
        })
        .then(response =>{
            dispatch(getAuthInfoSUCCESS(response.data))
        }).catch(error => {
            dispatch(getAuthInfoFAIL(error))
        })
    }
}
export const authLogin = (username, password) => {
    return dispatch =>{
        axios.post("http://127.0.0.1:8000/api/rest-auth/login/", {
            username: username,
            password: password
        })
        .then(response => {
            console.log(response.data);
            const token = response.data.key;
            const expirationDate = new Date(new Date().getTime() + 50000 * 1000);
            localStorage.setItem('token', response.data.key);
            localStorage.setItem('expirationDate', expirationDate);
            dispatch(getAuthInfo(token));
            dispatch(authSUCCESS(token));
            dispatch(checkTimeout(50000));  
        })
        .catch(error => {
            dispatch(authFAIL(error))
        })
    };
}

export const authSignUp = (username, email, password1, password2) => {
    return dispatch =>{
        axios.post("http://127.0.0.1:8000/api/rest-auth/registration/", {
            username: username,
            email: email,
            password1: password1,
            password2: password2
        })
        .then(response => {
            const token = response.data.key;
            const expirationDate = new Date(new Date().getTime() + 50000 * 1000);
            localStorage.setItem('token', response.data.key);
            localStorage.setItem('expirationDate', expirationDate);
            dispatch(getAuthInfo(token));
            dispatch(authSUCCESS(token));
            dispatch(checkTimeout(50000));
        })
        .catch(error => {
            dispatch(authFAIL(error))
        })
    };
}

export const checkTimeout = expirationTime=> {
    return dispatch => {
        setTimeout(() => {
            dispatch(authLOGOUT());   
        }, expirationTime * 1000)
    }
}


export const authLOGOUT = () =>{
    localStorage.removeItem('token');
    localStorage.removeItem('expirationDate');
    return {
        type: actionTypes.AUTH_LOGOUT
    };
}

export const isValid = () => {
    return dispatch => {
        const token = localStorage.getItem('token');
        if(token == undefined){
            dispatch(getAuthInfoSUCCESS("No user currently logged"))
            dispatch(authLOGOUT())
        }
        else{
            const expirationDate = new Date(localStorage.getItem('expirationDate'));
            if(expirationDate <= new Date()){
                dispatch(authLOGOUT())
            }else{
                axios.post("http://127.0.0.1:8000/api/CurrentUser/", {
                    token: token,
                })
                .then(response =>{
                    dispatch(getAuthInfoSUCCESS(response.data))
                }).catch(error =>{
                    dispatch(getAuthInfoFAIL(error))
                })
                dispatch(authSUCCESS(token));
                dispatch(checkTimeout( (expirationDate.getTime() - new Date().getTime() )/ 1000));
            }
        }
    }
}
