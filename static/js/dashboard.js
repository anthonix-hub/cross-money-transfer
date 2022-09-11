
const openMenu = document.querySelector('.open-menu');
const navBar = document.querySelector('.navbar');
const closeMenu = document.querySelector('.close-menu');
const logo = document.querySelector('.logo');

openMenu.addEventListener('click', () => {
    navBar.classList.add('active');
    closeMenu.style.display= "flex";
    openMenu.style.display = 'none';
    logo.style.display = 'none';

});

closeMenu.addEventListener('click', () => {
    navBar.classList.remove('active');
    closeMenu.style.display= "none";
    openMenu.style.display = 'flex';
    logo.style.display = 'flex';
})