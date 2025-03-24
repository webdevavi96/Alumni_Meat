import * as apiFn from './api.js';

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.querySelector('.loginForm');
  
  loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const email = document.querySelector('#email').value.trim();
    const password = document.querySelector('#password').value.trim();
    const messageBox = document.querySelector('.messageBox'); // Check for message box
    
    if (email && password) {
      const person = apiFn.getUser(email, password);
      try {
        const response = await apiFn.sendData(person);
        
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
          messageBox.innerHTML = `${error}`;
          messageBox.style.color = 'red';
        }
      }
    } else {
      if (messageBox) {
        messageBox.innerHTML = "Please enter a valid username or password!";
        messageBox.style.color = 'red';
      }
    }
  });
  
  /*registrain functions are here...*/
  const registrationForm = document.querySelector('.signInForm');
  
  registrationForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    
    const fullname = document.querySelector('#fullname').value.trim();
    const email = document.querySelector('#email').value.trim();
    const user_type = document.querySelector('#user_type').value;
    const branch = document.querySelector('#branch').value;
    const year = document.querySelector('#year').value;
    const enrollment = document.querySelector('#enrollment').value.trim();
    const password = document.querySelector('#password').value.trim();
    const rePassword = document.querySelector('#confirm_password').value.trim();
    const messageBox = document.querySelector('.messageBox');
    
    if (user_type == 'Student') {
      if (fullname && email && branch && year && user_type && enrollment && password && rePassword) {
        if (password === rePassword) {
          // Get the user object from `apiFn.newUser()`
          const person = apiFn.newUser(fullname, email, branch, enrollment, year, user_type, password);
          
          // Display the generated user object for debugging
          console.log("Generated User Object:", person);
          messageBox.innerHTML = JSON.stringify(person, null, 2); // Display user object in messageBox
          messageBox.style.color = "blue";
        }
        
        else {
          if (fullname && email && user_type && password && rePassword) {
            if (password === rePassword) {
              // Get the user object from `apiFn.newUser()`
              const person = apiFn.newAdmin(fullname, email, user_type, password);
            }
          }
        }
        try {
          // Assuming `newUserResponse(person)` sends data to the server
          const response = await newUserResponse(person);
          
          if (response.status === "success") {
            messageBox.innerHTML = "Account created successfully!";
            messageBox.style.color = "green";
          } else {
            messageBox.innerHTML = response.message || "Registration failed.";
            messageBox.style.color = "red";
          }
        } catch (e) {
          messageBox.innerHTML = `Error: ${e.message}`;
          messageBox.style.color = 'red';
        }
      } else {
        messageBox.innerHTML = "Passwords do not match";
        messageBox.style.color = 'red';
      }
    } else {
      messageBox.innerHTML = "Please fill all fields (Mandatory)";
      messageBox.style.color = "red";
    }
  });
  
  
  
  function toggleStudentDetails() {
    const isUser = document.querySelector('#user_type');
    const captureStudent = document.querySelector('.students_details');
    if (isUser == 'Student') {
      captureStudent.style.display = 'block';
    } else {
      captucptureStu.style.display = 'none';
    }
  }
});