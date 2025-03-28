export function getUser(email, password) {
  return {
    email: email,
    password: password
  };
}

export function newUser(fullname, email, branch, enrollment, year, user_type, password) {
  return {
    fullname,
    email,
    branch,
    enrollment,
    year,
    user_type,
    password
  };
}

export function newAdmin(fullname, email, user_type, password) {
  return {
    fullname,
    email,
    user_type,
    password
  };
}

export async function sendData(userData) {
  try {
    const response = await fetch("https://super-happiness-7vprqj4vw6pg2p474-8000.app.github.dev/api/verify_user/", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
      },
      body: JSON.stringify(userData)
    });
    return await response.json();
  } catch (error) {
    console.error("Login Error:", error);
    return { message: "Network error! Please try again." };
  }
}

export async function newUserResponse(newUserDetails) {
  try {
    const response = await fetch("https://super-happiness-7vprqj4vw6pg2p474-8000.app.github.dev/api/new_user/", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
      },
      body: JSON.stringify(newUserDetails)
    });
    return await response.json();
  } catch (error) {
    console.error("Registration Error:", error);
    return { message: "Network error! Please try again." };
  }
}

function getCSRFToken() {
  let cookieValue = null;
  const cookies = document.cookie ? document.cookie.split(';') : [];
  for (let cookie of cookies) {
    cookie = cookie.trim();
    if (cookie.startsWith('csrftoken=')) {
      cookieValue = cookie.substring('csrftoken='.length);
      break;
    }
  }
  return cookieValue || "";
}