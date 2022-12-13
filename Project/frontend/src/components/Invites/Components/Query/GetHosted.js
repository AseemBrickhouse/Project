import React, { useEffect, useState } from 'react';

export default function GetHosted() {
    const [data, setData] = useState()

    useEffect(async () =>{
        await fetch("http://127.0.0.1:8000/api/GetUserHostedGroups/", {
            method: "POST",
            headers: {
                'Accept':'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                token: localStorage.getItem('token')
            })
        })
        .then(response => {
            return response.json()
        })
        .then(data =>{
            setData(data)
        })
    },[])
    console.log(data)
    return data
}
