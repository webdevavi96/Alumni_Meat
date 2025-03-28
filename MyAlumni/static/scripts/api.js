export async function logInRequest(userData) {
  try {
    const response = await fetch("/verify_user/", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(userData)
    });
    return await response.json();
  } catch (error) {
    console.error("Login Error:", error);
    return { message: "Network error! Please try again." };
  }
}

export async function newUserRequest(newUserDetails) {
  try {
    const response = await fetch("/new_user", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(newUserDetails)
    });
    return await response.json();
  } catch (error) {
    console.error("Registration Error:", error);
    return { message: "Network error! Please try again." };
  }
}

// function getCSRFToken() {
//   let cookieValue = null;
//   const cookies = document.cookie ? document.cookie.split(';') : [];
//   for (let cookie of cookies) {
//     cookie = cookie.trim();
//     if (cookie.startsWith('csrftoken=')) {
//       cookieValue = cookie.substring('csrftoken='.length);
//       break;
//     }
//   }
//   return cookieValue || "";
// }