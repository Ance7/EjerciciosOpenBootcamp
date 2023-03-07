import React, {useState} from 'react';
import ContactForm from './contactForm';
import ContactList from './contactList';

const ContactApp = () => {

    const defaultContact = [
        {nombre: 'Contacto Ejemplo1', email: 'ejemplo1@gmail.com', conectado: true},
        {nombre: 'Contacto Ejemplo2', email: 'ejemplo2@gmail.com', conectado: false}
      ]
    
      const [nuevoContacto, setNuevoContacto] = useState(defaultContact)
    
      function changeState(contacto) {
        const index = nuevoContacto.indexOf(contacto)
        const tempContact = [...nuevoContacto]
        
        tempContact[index].estado = !tempContact[index].estado
        setNuevoContacto(tempContact)
      }
    
      function remove(contacto) {
        const index = nuevoContacto.indexOf(contacto)
        const tempContact = [...nuevoContacto]
        tempContact.splice(index, 1)
        setNuevoContacto(tempContact)
      }
    
      function addContact(contacto) {
        const tempContact = [...nuevoContacto]
        tempContact.push(contacto)
        setNuevoContacto(tempContact)
      }

    return (
        <div>
            <h1>Contactos</h1>

      <div className='card-container'>
        {nuevoContacto.map((contacto, index) => {
          return (<ContactList key={index} contacto={contacto} changeState={changeState} remove={remove}/>)
        })}
      </div>
        <ContactForm onAddContact={addContact}></ContactForm>
        </div>
    );
}

export default ContactApp;
