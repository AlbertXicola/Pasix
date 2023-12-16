import React, { useState } from 'react';
import '../css/01-login.css';

const Login = ({ handleMenuClick }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showMainMenuButton, setShowMainMenuButton] = useState(true);


  const handleLogin = () => {
    // Aquí puedes implementar la lógica de autenticación
    console.log(`Usuario: ${username}, Contraseña: ${password}`);
    // Después del inicio de sesión, cambia al menú principal (Inicio)
  };

  const handleMainMenuClick = () => {
    // Cambia al menú principal (Inicio)
    handleMenuClick('Inicio');
  };

  return (
    <div className="login-container">
      <button className="close-button" type="button" onClick={handleMainMenuClick}>
        X
      </button>
      <h2 className="login-h2">Iniciar Sesión</h2>
      <form className="login-form">
        <label className="login-label">
        
          <input placeholder='Usuario'
            className="login-input"
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <label className="login-label">

          <input placeholder='Contraseña'
            className="login-input"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <button className="login-button" type="button" onClick={handleLogin}>
          Iniciar Sesión
        </button>
      </form>
    </div>
  );
};

export default Login;
