const ButtonChangeTheme = document.querySelector('.change-theme');
const Theme = localStorage.getItem('theme');
const Page = document.querySelector('body');
const Header = document.querySelector('header');
const Footer = document.querySelector('footer');
const NavItems = document.querySelectorAll('.navbar-link');
const Copyright = document.querySelector('.copyright');
const Logo = document.querySelector('.logo');
const Cards = document.querySelectorAll('.portfolio-card');
const Post = document.querySelector('.postpage');


if (Theme) {
    Page.setAttribute('dark-theme', 'yes');
    ButtonChangeTheme.src = "/static/images/light.svg";
    Header.setAttribute('dark-theme', 'yes');
    Footer.setAttribute('dark-theme', 'yes');
    Copyright.setAttribute('dark-theme', 'yes');
    for (var i = 0; i < NavItems.length; i++) {
        NavItems[i].setAttribute('dark-theme', 'yes');
    }
    if (Logo) {
            Logo.setAttribute('dark-theme', 'yes');
        }
    for (var i = 0; i < Cards.length; i++) {
        Cards[i].setAttribute('dark-theme', 'yes');
    }
    if (Post) {
        Post.setAttribute('dark-theme', 'yes');
    }
} 

ButtonChangeTheme.addEventListener('click',  () => {
    if (Page.getAttribute('dark-theme')) {
        Page.removeAttribute('dark-theme');
        ButtonChangeTheme.src = "/static/images/dark.svg";
        ButtonChangeTheme.removeAttribute('dark-theme');
        Header.removeAttribute('dark-theme');
        Footer.removeAttribute('dark-theme');
        Copyright.removeAttribute('dark-theme');
        NavItems[5].removeAttribute('dark-theme');
        for (var i = 0; i < NavItems.length; i++) {
        NavItems[i].removeAttribute('dark-theme');
        }
        if (Logo) {
            Logo.removeAttribute('dark-theme');
        }
        for (var i = 0; i < Cards.length; i++) {
        Cards[i].removeAttribute('dark-theme');
        }
        if (Post) {
            Post.removeAttribute('dark-theme');
        }
        
        localStorage.removeItem('theme');
    } else {
        Page.setAttribute('dark-theme', 'yes');
        ButtonChangeTheme.setAttribute('dark-theme', 'yes');
        ButtonChangeTheme.src = "/static/images/light.svg";
        Header.setAttribute('dark-theme', 'yes');
        Footer.setAttribute('dark-theme', 'yes');
        Copyright.setAttribute('dark-theme', 'yes');
        for (var i = 0; i < NavItems.length; i++) {
            NavItems[i].setAttribute('dark-theme', 'yes');
        }
        if (Logo) {
            Logo.setAttribute('dark-theme', 'yes');
        }
        for (var i = 0; i < Cards.length; i++) {
        Cards[i].setAttribute('dark-theme', 'yes');
        }
        if (Post) {
        Post.setAttribute('dark-theme', 'yes');
        }

        localStorage.setItem('theme', 'dark-theme');
    }
} )
