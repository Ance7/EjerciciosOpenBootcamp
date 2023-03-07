import React, { useState, useEffect } from 'react';

const Clock = () => {

    const [fecha, setFecha] = useState(new Date());
    const [edad, setEdad] = useState(0);
    const [nombre] = useState('Martin');
    const [apellidos] = useState('San Jose');

    useEffect(() => {
        const timerID = setInterval(tick, 1000)
        
        return() => clearInterval(timerID)
    });
    
    
    function tick() {
        setFecha(new Date())
        setEdad(edad + 1)
    }
    return (
        <div>
            <h2>
                Hora Actual: 
                { fecha.toLocaleTimeString() }
            </h2>
            <h3>
                { nombre } { apellidos }
            </h3>
            <h1>
                Edad: { edad }
            </h1>
        </div>
    );
}

export default Clock;
