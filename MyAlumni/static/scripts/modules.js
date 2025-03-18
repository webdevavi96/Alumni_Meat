import * as apiFn from './api.js';

async function getData() {
  const dataFromAPI = await apiFn.test();
  alert(dataFromAPI.message); // Now inside function
}

getData();