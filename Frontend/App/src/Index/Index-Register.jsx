import React, { useState } from 'react';
import '../css/01-register.css';

const Register = ({ handleMenuClick }) => {
  const [nombre, setNombre] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showMainMenuButton, setShowMainMenuButton] = useState(true);
  const [errorEmail, setErrorEmail] = useState('');
  const [errorPassword, setErrorPassword] = useState('');

  const handleRegister = () => {
    // Validar el formato del correo electrónico
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setErrorEmail('Por favor, introduce un correo electrónico válido.');
      return;
    }

    // Validar la contraseña
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$/;
    if (!passwordRegex.test(password)) {
      setErrorPassword('La contraseña debe tener al menos 10 caracteres, incluyendo mayúsculas, minúsculas, números y caracteres especiales.');
      return;
    }

    const userData = {
      nombre: nombre,
      email: email,
      password: password,
    };

    fetch('http://localhost:8000/usuarios/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    })
      .then(response => response.json())
      .then(data => {
        console.log('Registro exitoso:', data);
        // Redirigir al usuario a otra página
        window.location.href = '/user';
      })
      .catch(error => console.error('Error en el registro:', error));
  };

  const handleMainMenuClick = () => {
    // Volver al menú principal
    handleMenuClick('Inicio');
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
    // Limpiar el mensaje de error al cambiar el correo electrónico
    setErrorEmail('');
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
    // Limpiar el mensaje de error al cambiar la contraseña
    setErrorPassword('');
  };

  return (
    <div className="register-container">
      {showMainMenuButton && (
        <button className="close-button" type="button" onClick={handleMainMenuClick}>
          boton oculto
        </button>
      )}
      <h2 className="register-h2">Registro</h2>
      <form className="register-form">
        <label className="register-label">
          <input
            placeholder="Nombre"
            className="register-input"
            type="text"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
          />
        </label>
        <label className="register-label">
          <input
            placeholder="Email"
            className="register-input"
            type="email"
            value={email}
            onChange={handleEmailChange}
          />
        </label>
        {errorEmail && <p className="error-message">{errorEmail}</p>}
        <label className="register-label">
          <input
            placeholder="Password"
            className="register-input"
            type="password"
            value={password}
            onChange={handlePasswordChange}
          />
        </label>
        {errorPassword && <p className="error-message">{errorPassword}</p>}
        <button className="register-button" type="button" onClick={handleRegister}>
          Registrarse
        </button>
      </form>
    </div>
  );
};

export default Register;
