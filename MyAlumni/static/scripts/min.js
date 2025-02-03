document.addEventListener("DOMContentLoaded", function () {
    let currentPath = window.location.pathname;
    let navLinks = document.querySelectorAll(".nav-link");

    navLinks.forEach(link => {
      if (link.getAttribute("href") === currentPath) {
        link.classList.add("active");
      }
    });
  });