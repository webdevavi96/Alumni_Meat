// document.addEventListener('DOMContentLoaded', () => {
//   const navLinks = document.querySelectorAll('.nav-link');

//   navLinks.forEach((link) => {
//     link.addEventListener('click', (event) => {
//       event.preventDefault();
//       navLinks.forEach(nav => nav.classList.remove('active'));
//       link.classList.add('active');

//       const requestUrl = link.getAttribute('href');
//       fetch(requestUrl)
//         .then(response => response.text())
//         .then(data => {
//           document.getElementById('content').innerHTML = data;
//         })
//         .catch(error => console.error('Error loading content:', error));
//     });
//   });

//   const activeLink = window.location.pathname;
//   navLinks.forEach((link) => {
//     if (link.getAttribute('href') === activeLink) {
//       link.classList.add('active');
//     }
//   });
// });