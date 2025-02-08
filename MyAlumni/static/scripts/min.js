//js loading screen
const loaderItem = document.querySelector('.loader');
const bodyElements = document.querySelector('.loaded');
function loader() {
  bodyElements.style.display = 'block'
  loaderItem.style.display = 'none'

}

//js for user profile
const userProfile = document.querySelector('.profile');
function triggerUser() {
  userProfile.addEventListener('click', () => {
      window.location.href = profilrUrl;
  });
}

//all function will run after the page fully loaded
document.addEventListener('DOMContentLoaded', () => {
  const navLinks = document.querySelectorAll('.nav-link');

  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      navLinks.forEach(nav => nav.classList.remove('active'));
      link.classList.add('active');
    });
  });

  const activeLink = window.location.pathname;
  navLinks.forEach((link) => {
    if (link.getAttribute('href') === activeLink) {
      link.classList.add('active');
    }
  });
  
  //loading screen timeout function
  setTimeout(() => {
     loader();
  }, 1000);
  
  
  //user profile navigation function
  triggerUser();
});

