import * as React from 'react';
import styles from "./css/loading.module.css"
import Spinner from 'react-bootstrap/Spinner';

export const Loading = () => {
    return(
        <div className={styles.containerMain}>
          <div className={styles.subcontainer}>
            <div style={{marginLeft: "3vw"}}>
              <div className={styles.header}>
                Place holder
              </div>
            </div>
            <div style={{marginLeft: "5vw"}}>
              <div className={styles.body}>
                Quote
              </div>
            </div>
            <div style={{textAlign: "right", marginRight: "5vw"}}>
              <div className={styles.footer}>
                Word
              </div>
            </div>
            <div style={{marginLeft: "3vw"}}>
              <div>
                <span className={styles.rotatingTextAdjective}>Verfiying</span>
                <span className={styles.rotatingTextAdjective}>Success!</span>
              </div>
            </div>
            <div className={styles.loading}>
                <span className={styles.spinner}><Spinner animation="border" size="50px"/></span>
            </div>
          </div>
        </div>
    )
}
export default Loading;