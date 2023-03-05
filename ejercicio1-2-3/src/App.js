import logo from './logo.svg';
import './App.css';
import ContactoConectado from './Components/container/contacto_conectado';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <ContactoConectado />
      </header>
    </div>
  );
}

export default App;
