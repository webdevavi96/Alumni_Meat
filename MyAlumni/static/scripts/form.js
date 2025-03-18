
document.addEventListener("DOMContentLoaded", function() {
  const newAccount = document.querySelector('.newAccount'); // Corrected selector
  const loginForm = document.querySelector('.loginForm');
  const resetLink = document.querySelector('.resetPassword');
  const newUserForm = document.querySelector('.newUserForm');
  const loginLink = document.querySelector('.loginLink'); // New element to go back to login

  // Hide the new user form initially
  newUserForm.style.display = "none";

  // Function to show registration form
  function showRegistrationForm() {
    loginForm.style.display = "none";
    resetLink.style.display = "none";
    newUserForm.style.display = "block";
    // console.log("hello")
  }

  // Function to show login form again
  function showLoginForm() {
    newUserForm.style.display = "none";
    loginForm.style.display = "block";
    resetLink.style.display = "block";
  }

  // Event listeners for toggling forms
  newAccount.addEventListener('click', showRegistrationForm);
  loginLink.addEventListener('click', showLoginForm);
});