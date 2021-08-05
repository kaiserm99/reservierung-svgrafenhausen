// Get the needed elements
const burger = document.querySelector(".nav-button");
const nav = document.querySelector(".nav-links");
let navLink = document.querySelectorAll(".nav-link");

const homeUrl = "/";

const navSlide = () => {

  // Event Listener which will execute the Code in the function
  burger.addEventListener("click", () => {
    // Toggle navbar
    nav.classList.toggle("nav-active");
    burger.classList.toggle("nav-active");
  });
}

// Make sure there is no height gap when the chrome browser has a adressbar
const activeNavHeight = () => {
  let vh = window.innerHeight * 0.01;
  document.documentElement.style.setProperty('--vh', `${vh}px`);

  // Listen to the resize event
  window.addEventListener('resize', () => {
    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
  });
}


navLink[0].addEventListener('click', () => {
  window.location.replace(homeUrl);
});

// Put main function call here:
navSlide();
activeNavHeight();