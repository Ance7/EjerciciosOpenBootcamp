import React from 'react';
import { Contacto } from '../../models/componenteA.class';
import ComponenteB from '../pure/componenteB';

const ContactoConectado = () => {
    
    const contactoPersona = new Contacto('Anghelo', 'Alva', 'ance.anghelo@gmail.com', true)

    return (
        <div>
            <ComponenteB contacto={contactoPersona}/>
        </div>

    );
};


ContactoConectado.propTypes = {

};


export default ContactoConectado;
