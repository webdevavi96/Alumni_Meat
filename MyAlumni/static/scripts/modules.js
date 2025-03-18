import * as apiFn from './api.js';

async function getData() {
  const dataFromAPI = await apiFn.test();
  alert(dataFromAPI.message); // Now inside function
}

getData();



document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.querySelector('.userForm')
  loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const email = document.querySelector('#email').value.trim();
    const password = document.querySelector('#password').value.trim();
    if (email && password) {
      const person1 = apiFn.getUser(email, password);
      const response = await apiFn.sendData(person1)
      if (response.status === "success") {
        document.querySelector('.messageBox').innerHTML = "Logged in Successfully!";
        document.querySelector('.messageBox').style.color = 'green';
        console.log("Logged In")
      } else {
        console.log("username or password are Incorrect!")
      }
    } else {
      document.querySelector('.messageBox').innerHTML = "username or password is Invalid!";
      document.querySelector('.messageBox').style.color = 'red';
    }
  });
});