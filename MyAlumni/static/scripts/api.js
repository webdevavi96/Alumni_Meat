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