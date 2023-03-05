import React from 'react';
import PropTypes from 'prop-types';
import { Contacto } from '../../models/componenteA.class';

const ComponenteB = ({ contacto }) => {
    return (
        <div>
            <h1>
                La persona de nomrbe { contacto.nombre } { contacto.apellido }
            </h1>
            <h3>
                con email {contacto.email} esta {contacto.conectado ? 'Conectado':'Desconectado'}
            </h3>
        </div>
    );
};


ComponenteB.propTypes = {
    contacto: PropTypes.instanceOf(Contacto)
};


export default ComponenteB;
