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
});