const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');
const homeContent = document.querySelector('.home-content');
const aboutContent = document.querySelector('.about-content');
const projectContent = document.querySelector('.project-content');

registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');
    homeContent.classList.add('hidden');
    aboutContent.classList.add('hidden');
    projectContent.classList.add('hidden');
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
    homeContent.classList.ads('hidden');
    aboutContent.classList.add('hidden');
    projectContent.classList.add('hidden');
});

btnPopup.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
    homeContent.classList.add('hidden');
    aboutContent.classList.add('hidden');
    projectContent.classList.add('hidden');
});

iconClose.addEventListener('click', () => {
    wrapper.classList.remove('active-popup', 'active');
    homeContent.classList.remove('hidden');
    aboutContent.classList.add('hidden');
    projectContent.classList.add('hidden');
});

document.addEventListener('DOMContentLoaded', function() {
    // Oculta los contenidos de "About" y "Project" al cargar la página
    aboutContent.classList.add('hidden');
    projectContent.classList.add('hidden');

    // Nuevos listeners para los botones de navegación
    document.querySelector('nav').addEventListener('click', (event) => {
        if (event.target.tagName === 'A') {
            const contentToShow = event.target.textContent.toLowerCase();
            hideAllContent();
            document.querySelector(`.${contentToShow}-content`).classList.remove('hidden');
        }
    });

    function hideAllContent() {
        homeContent.classList.add('hidden');
        aboutContent.classList.add('hidden');
        projectContent.classList.add('hidden');
    }
  
    // Mostrar el contenido de "Home" al cargar la página
    homeContent.classList.remove('hidden');
    
    // Nuevos listener para el enlace "Home" dentro del contenido de "Login"
    const homeLinkInLogin = document.querySelector('.login-content .home-link');
  
    if (homeLinkInLogin) {
        homeLinkInLogin.addEventListener('click', () => {
            // Ocultar el contenido de "Login" al hacer clic en "Home"
            homeContent.classList.remove('hidden');
            loginContent.classList.add('hidden');
        });
    }
});
const loginPasswordInput = document.getElementById('loginPassword');
const toggleLoginButton = document.getElementById('toggleLoginPassword');

let isLoginMouseDown = false;

toggleLoginButton.addEventListener('mousedown', function () {
    isLoginMouseDown = true;
    loginPasswordInput.setAttribute('type', 'text');
});

toggleLoginButton.addEventListener('mouseup', function () {
    isLoginMouseDown = false;
    loginPasswordInput.setAttribute('type', 'password');
});

toggleLoginButton.addEventListener('mouseout', function () {
    if (isLoginMouseDown) {
        isLoginMouseDown = false;
        loginPasswordInput.setAttribute('type', 'password');
    }
});
