// App.js
import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import MainMenu from "./Index/Index-MainMenu";
import Login from "./Index/Index-Login";
import Register from "./Index/Index-Register";
// import UserMenu from "./Index-UserMenu";
import HomeContent from "./Index/Index-HomeContent";

const components = {
  Inicio: null,
  Registrarse: <Register />,
  "Iniciar Sesión": <Login />,
};

const App = () => {
  const [currentObject, setCurrentObject] = useState("Inicio");

  const handleMenuClick = (object) => {
    setCurrentObject(object);
  };

  return (
    <React.StrictMode>
      <MainMenu handleMenuClick={handleMenuClick} />
      {components[currentObject] || components.default}
      {currentObject === "Inicio" && <HomeContent />}
    </React.StrictMode>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);