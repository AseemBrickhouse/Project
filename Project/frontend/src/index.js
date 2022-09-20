import App from './components/App';
import React from 'react';
import ReactDOM from 'react-dom';
//    import rootReducer from './store/reducers';
//   import { configureStore, compose, applyMiddleware} from 'redux';     
import thunk from 'redux-thunk';
import { Provider } from 'react-redux';

//    const composeEnhances = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
//   const store = configureStore(rootReducer, composeEnhances(
//       applyMiddleware(thunk)
//   ));

const app = (
       // <Provider store = {store}>
       //     <App/>
       // </Provider>
        <div>
            <App/>
        </div>
)

ReactDOM.render(app, document.getElementById('app'));