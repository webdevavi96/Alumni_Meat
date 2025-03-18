export async function test(){
  const response = await fetch("https://super-happiness-7vprqj4vw6pg2p474-8000.app.github.dev/api/data/")
  const data = await response.json()
  .catch(error)
  console.log(error)
 return data
}