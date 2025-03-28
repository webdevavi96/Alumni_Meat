document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.querySelector('.loginForm');
  
  loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const email = document.querySelector('#login_email').value.trim();
    const password = document.querySelector('#login_password').value.trim();
    const messageBox = document.querySelector('.messageBox');
    
    if (email && password) {
      const person = apiFn.getUser(email, password);
      try {
        const response = await apiFn.sendData(person);
        if (response.status === "success") {
          window.location.href = '/';
        } else {
          messageBox.innerHTML = "Username or password is incorrect!";
          messageBox.style.color = 'red';
        }
      } catch (error) {
        messageBox.innerHTML = 'Something went wrong! Please try again.';
        messageBox.style.color = 'red';
      }
    } else {
      messageBox.innerHTML = "Please fill in both fields!";
      messageBox.style.color = 'red';
    }
  });
  
  /* Registration Logic */
  const registrationForm = document.querySelector('.signInForm');
  
  registrationForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    
    const fullname = document.querySelector('#fullname').value.trim();
    const email = document.querySelector('#email').value.trim();
    const user_type = document.querySelector('#user_type').value;
    const branch = document.querySelector('#branch').value || "";
    const year = document.querySelector('#year').value || "";
    const enrollment = document.querySelector('#enrollment').value.trim() || "";
    const password = document.querySelector('#password').value.trim();
    const rePassword = document.querySelector('#confirm_password').value.trim();
    const messageBox = document.querySelector('.messageBox');
    let person = null;
    
    if (password !== rePassword) {
      messageBox.innerHTML = "Passwords do not match";
      messageBox.style.color = 'red';
      return;
    }
    
    if (user_type === 'Student') {
      if (fullname && email && branch && year && enrollment && password) {
        person = apiFn.newUser(fullname, email, branch, enrollment, year, user_type, password);
      } else {
        messageBox.innerHTML = "Please fill all mandatory fields!";
        messageBox.style.color = 'red';
        return;
      }
    } else if (user_type === 'Admin') {
      if (fullname && email && password) {
        person = apiFn.newAdmin(fullname, email, user_type, password);
      } else {
        messageBox.innerHTML = "Please fill all mandatory fields!";
        messageBox.style.color = 'red';
        return;
      }
    }
    
    try {
      const response = await apiFn.newUserResponse(person);
      if (response.status === "success") {
        window.location.href = '/login/';
      } else {
        messageBox.innerHTML = response.message || "Registration failed.";
        messageBox.style.color = "red";
      }
    } catch (e) {
      messageBox.innerHTML = `Error: ${e.message}`;
      messageBox.style.color = 'red';
    }
  });
});

