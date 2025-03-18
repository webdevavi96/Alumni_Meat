import * as apiFn from './api.js';


document.addEventListener('DOMContentLoaded', () => {
  const loaderItem = document.querySelector('.loader');
  const bodyElements = document.querySelector('.loaded');
  const body = document.body;
  const navLinks = document.querySelectorAll('.nav-link');

  // Function to hide loader and show content
  function loader() {
    if (bodyElements) bodyElements.style.display = 'block';
    if (loaderItem) loaderItem.style.display = 'none';
  }

  // Navigation link active state handling
  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      navLinks.forEach(nav => nav.classList.remove('active'));
      link.classList.add('active');
    });
  });

  // Set active link based on current page URL
  const activeLink = window.location.pathname;
  navLinks.forEach((link) => {
    if (link.getAttribute('href') === activeLink) {
      link.classList.add('active');
    }
  });

  // Add profileBody class if the user is on the profile page
  if (activeLink.includes('profile')) {
    body.classList.add('profileBody');
  }

  // Loading screen timeout function
  setTimeout(loader, 1000);
  
  
  apiFn.greet()
});