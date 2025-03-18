import * as apiFn from './api.js';

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
        } else {
          if (messageBox) {
            messageBox.innerHTML = "Username or password is incorrect!";
            messageBox.style.color = 'red';
          }
        }
      } catch (error) {
        if (messageBox) {
          messageBox.innerHTML =`${error}`;
          messageBox.style.color = 'red';
        }
      }
    } else {
      if (messageBox) {
        messageBox.innerHTML = "Please enter a valid username or password!";
        messageBox.style.color = 'orange';
      }
    }
  });
});



// async function getData() {
//   const dataFromAPI = await apiFn.test();
//   alert(dataFromAPI.message); // Now inside function
// }

// getData();