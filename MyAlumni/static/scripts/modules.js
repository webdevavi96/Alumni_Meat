import * as apiFn from './api.js';

async function getData() {
  const dataFromAPI = await apiFn.test();
  alert(dataFromAPI.message); // Now inside function
}

getData();




document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.querySelector('.userForm');
  
  loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const email = document.querySelector('#email').value.trim();
    const password = document.querySelector('#password').value.trim();
    const messageBox = document.querySelector('.messageBox'); // Check for message box
    
    if (email && password) {
      const person1 = apiFn.getUser(email, password);
      try {
        const response = await apiFn.sendData(person1);
        
        if (response.status === "success") {
          if (messageBox) {
            messageBox.innerHTML = "Logged in Successfully!";
            messageBox.style.color = 'green';
          }
          alert("Logged In");
        } else {
          if (messageBox) {
            messageBox.innerHTML = "Username or password is incorrect!";
            messageBox.style.color = 'red';
          }
     alert("Username or password is incorrect!");
        }
      } catch (error) {
       alert("Error:", error);
        if (messageBox) {
          messageBox.innerHTML = "Something went wrong! Please try again.";
          messageBox.style.color = 'red';
        }
      }
    } else {
      if (messageBox) {
        messageBox.innerHTML = "Username or password is invalid!";
        messageBox.style.color = 'red';
      }
    }
  });
});