export async function test() {
  try {
    const response = await fetch("https://super-happiness-7vprqj4vw6pg2p474-8000.app.github.dev/api/data/");
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    return { message: "Error fetching data" }; // Return default message
  }
}

export function getUser(email, password) {
  let userDetails = {
    "email": email,
    "password": password
  }
  return userDetails;
}

export async function sendData(userData) {
  try {
    const serverResponse = await fetch("https://super-happiness-7vprqj4vw6pg2p474-8000.app/api/varify_user/", {
      method: 'POST',
      headers: {
        'Content-Type': 'aplication/json',
        'X-CSRFToken': getCSRFToken()
      },
      body: JSON.stringify(userData)
    });
    
    const rData = await serverResponse.json();
    return rData;
  } catch (e) {
    throw e
  }
}


function getCSRFToken() {
  let cookieValue = null;
  const cookies = document.cookie.split(';');
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.startsWith('csrftoken=')) {
      cookieValue = cookie.substring('csrftoken='.length, cookie.length);
      break;
    }
  }
  return cookieValue;
}