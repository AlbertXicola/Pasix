import React, { useState } from 'react';
import '../css/01-HomeContent.css'; // Asegúrate de tener el archivo de estilos adecuado

const HomeContent = () => {
  const quotesWithAuthors = [
    { quote: "Buenas Tardes", author: "- yo por las tardes", image: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.britannica.com%2F40%2F144440-050-DA828627%2FMorgan-Freeman.jpg&f=1&nofb=1&ipt=2455d05295054707481508517fe374840a1b684b626db47a9d5e076e155f99ed&ipo=images" },
    // { quote: "Pocas veces pensamos en lo que tenemos; pero siempre en lo que nos falta", author: "- Schopenhauer", image: "https://perithorio.com/wp-content/uploads/2021/07/Arthur_Schopenhauer_by_J_Schafer_1859b.jpg" },
    // { quote: "La medida del amor es amar sin medida.", author: "- San Agustín de Hipona", image: "https://pymstatic.com/29604/conversions/san-agustin-hipona-social.jpg" },
    // { quote: "La fe busca, la inteligencia encuentra.", author: "- San Agustín de Hipona", image: "https://pymstatic.com/29604/conversions/san-agustin-hipona-social.jpg" },
    // { quote: "Ama y haz lo que quieras.", author: "- San Agustín de Hipona", image: "https://pymstatic.com/29604/conversions/san-agustin-hipona-social.jpg" },
    // { quote: "La oración es el lugar de refugio para cada preocupación, una base para la felicidad, un lugar de descanso para la ansiedad.", author: "- San Juan Crisóstomo", image: "https://www.religiondigital.org/2020/09/12/un_santo_para_cada_dia/San-Juan-Crisostomo_2267783227_14901902_667x375.jpg" },
    // { quote: "La paciencia es la compañera del sabio.", author: "- San Agustín de Hipona", image: "https://pymstatic.com/29604/conversions/san-agustin-hipona-social.jpg" },
    // { quote: "La humildad es la base de todas las virtudes.", author: "- San Agustín de Hipona", image: "https://pymstatic.com/29604/conversions/san-agustin-hipona-social.jpg" },
    // { quote: "La fe y la razón son como las dos alas de un pájaro; sin ambas, el hombre no puede volar.", author: "- San Juan Pablo II", image: "https://desdelafe.mx/wp-content/uploads/2020/05/san-juan-pablo-ii-768x511.jpg" },
    // { quote: "La verdadera medida del amor es amar sin medida.", author: "- San Francisco de Asís", image: "https://www.rincondelafe.com/wp-content/uploads/2015/08/san-francisco-de-asis-biografia.jpg" },
    // { quote: "No midas la oración por su longitud, sino por su fervor.", author: "- San Juan Crisóstomo", image: "https://www.religiondigital.org/2020/09/12/un_santo_para_cada_dia/San-Juan-Crisostomo_2267783227_14901902_667x375.jpg" },
    // { quote: "La gracia es amor que se muestra incluso cuando no es merecido.", author: "- San Agustín de Hipona", image: "https://pymstatic.com/29604/conversions/san-agustin-hipona-social.jpg" },
  ];
 

  const [randomQuote, setRandomQuote] = useState('');

  const getRandomQuote = () => {
    const randomIndex = Math.floor(Math.random() * quotesWithAuthors.length);
    setRandomQuote(quotesWithAuthors[randomIndex]);
  };

  // Llama a getRandomQuote cuando el componente se monta
  useState(() => {
    getRandomQuote();
  }, []);

  return (
    <div className="home-content-container">
      <img src={randomQuote.image} alt="Imagen del autor" className="home-image" />
      <div className="home-text">
        <h3 className="quote">{randomQuote.quote}</h3>
        <p className="author">{randomQuote.author}</p>
      </div>
    </div>
  );
};

export default HomeContent;
