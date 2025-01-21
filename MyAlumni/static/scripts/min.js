const navBtn = document.querySelector('.nav-btn');

function navExpand() {
  const navItems = document.querySelector('.nav-menu-items');
  if (navItems) {
    navItems.classList.toggle('active'); // Toggle class
  }
  console.log('Clicked');
}

if (navBtn) {
  navBtn.addEventListener('click', navExpand);
}