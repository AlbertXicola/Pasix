// Index-App-user.jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import UserMenu from './Usuario/Index-UserMenu'
// Importa otros componentes según sea necesario

const IndexAppUser = () => {
  // Puedes obtener la información del usuario, por ejemplo, desde la API o almacenamiento local.
  const userData = {
    nombre: 'Nombre del Usuario',
    // Otros datos del usuario
  };

  return (
    <React.StrictMode>
      {/* Puedes agregar más componentes según sea necesario */}
      <UserMenu userData={userData} />
      {/* Otros componentes aquí */}
    </React.StrictMode>
  );
};

ReactDOM.createRoot(document.getElementById('root')).render(<IndexAppUser />);

