import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";

const ScholarShipInformation = (props) => {
    return (            
        <body>
          <div className="container">
            <div className="info-box">
              <form className="info">
                <div className="elements">
                  <h1>Scholarship Name</h1>
                  <p>Scholarship Provider Name</p>
                </div>
                <div className="elements">
                  <button className="full-btn">Collapseable button</button>
                </div>
                <div className="elements">
                  <p>Scholarship Description: This is a cool one to apply for because it'll allow you to get money.</p>
                </div>
                <div className="elements">
                  <p>Scholarship Requirements:</p>
                  <p>&#8226; Requirement</p>
                  <p>&#8226; Requirement</p>
                  <p>&#8226; Requirement</p>
                </div>
            
                <div className="elements">
                  <button className="full-btn">Apply!</button>
                </div>
              </form>
            </div>
          </div>
        </body>
    );
}

export default ScholarShipInformation;