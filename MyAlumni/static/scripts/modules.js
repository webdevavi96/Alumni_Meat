import * as apiFn from './api.js';


document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('.loginForm').addEventListener('submit', (event) => {
    event.preventDefault();
    logIn();
  });
  
  document.querySelector('.signInForm').addEventListener('submit', (event) => {
    event.preventDefault();
    registerNewUser();
  });
});


async function logIn() {
  const loginEmail = document.querySelector('#login_email');
  const loginPassword = document.querySelector('#login_password');
  const messageBox = document.querySelector('.messageBox');
  if (loginEmail && loginPassword) {
    const user = {
      'email': loginEmail,
      'password': loginPassword
    }
    try {
      const response = await apiFn.logInRequest(user)
      if (response.status == "success") {
        window.locatior.href = "/";
      }
    } catch (e) {
      messageBox.innerHTML = "Something went wrong!  Please try after sometime.."
      messageBox.style.color = 'red';
    }
  }
  else {
    messageBox.innerHTML = "Email or Password didn’t matched!"
    messageBox.style.color = 'red';
  }
}


async function registerNewUser() {
  const fullname = document.querySelector('#fullname').value.trim();
  const email = document.querySelector('#email').value.trim();
  const user_type = document.querySelector('#user_type').value;
  const password = document.querySelector('#password').value.trim();
  const rePassword = document.querySelector('#confirm_password').value.trim();
  const messageBox = document.querySelector('.messageBox');
  
  if (user_type == "Admin" || user_type == "Alumni") {
    if (fullname && email && password) {
      const newUser = {
        'fullname': fullname,
        'email': email,
        'user_type': user_type,
        'password': password
      }
      
      try {
        const response = await apiFn.newUserRequest(newUser)
        if (response.status == "success") {
          window.location.href = '/login/';
        }
      } catch (e) {
        messageBox.innerHTML = "Something went wrong!  Please try after sometime.."
        messageBox.style.color = 'red';
      }
    }
  }
  else {
    const branch = document.querySelector('#branch').value || "";
    const year = document.querySelector('#year').value || "";
    const enrollment = document.querySelector('#enrollment').value.trim() || "";
    
    if (fullname && email && password && branch && year && enrollment) {
      if (password === rePassword) {
        const newStudent = {
          'fullname': fullname,
          'email': email,
          'password': password,
          'user_type': user_type,
          'branch': branch,
          'year': year,
          'enrollment': enrollment
        }
        try {
          const response = await apiFn.newUserRequest(newStudent);
          if (response.status == "success") {
            window.location.href = '/login/'
          }
        } catch (e) {
          messageBox.innerHTML = "Something went wrong!  Please try after sometime.."
          messageBox.style.color = 'red';
        }
        
      }
      else {
        messageBox.innerHTML = "Password didn’t matched!..."
        messageBox.style.color = 'red';
      }
    } else {
      messageBox.innerHTML = "Pleasefill all Mandatory fields!..."
      messageBox.style.color = 'red';
    }
    
  }
}
