import React from 'react';
import '../css/01-mainmenu.css';

const MainMenu = ({ handleMenuClick }) => {
  return (
    <div className="menu-container">
      <button className="menu-button" onClick={() => handleMenuClick('Inicio')}>
        Inicio
      </button>
      <button className="reg-button" onClick={() => handleMenuClick('Registrarse')}>
        Registrarse
      </button>
      <button className="login1-button" onClick={() => handleMenuClick('Iniciar Sesión')}>
        Iniciar Sesión
      </button>
    </div>
  );
};

export default MainMenu;
