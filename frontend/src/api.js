import axios from 'axios';

// Backend API'mizin temel adresini tanımlıyoruz
const api = axios.create({
  baseURL: 'http://localhost:8000/api', // FastAPI sunucu adresimiz
});

export default api;