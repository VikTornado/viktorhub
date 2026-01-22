import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api',
});

export const getProjects = (params) => api.get('/projects/', { params });
export const getProject = (slug) => api.get(`/projects/${slug}/`);
export const getPosts = (params) => api.get('/posts/', { params });
export const getPost = (slug) => api.get(`/posts/${slug}/`);
export const getNotes = (params) => api.get('/notes/', { params });
export const getTags = () => api.get('/tags/');
export const sendContact = (data) => api.post('/contact/', data);

export default api;
