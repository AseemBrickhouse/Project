import App from './components/App';
import React from 'react';
import ReactDOM from 'react-dom';
import rootReducer from './store/reducers';
import { createStore, compose, applyMiddleware} from 'redux';     
import thunk from 'redux-thunk';
import { Provider } from 'react-redux';

const composeEnhances = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(rootReducer, composeEnhances(
    applyMiddleware(thunk)
));

const app = (
       <Provider store = {store}>
           <App/>
       </Provider>
)

ReactDOM.render(app, document.getElementById('app'));