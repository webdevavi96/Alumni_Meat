import * as apiFn from './api.js';

async function getData() {
  const dataFromAPI = await apiFn.test()
  return dataFromAPI
}

getData()
alert(dataFromAPI.message)