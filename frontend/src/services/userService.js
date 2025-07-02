import api from './api';

export const loginUser = (credentials) => {
  return api.post('/users/login/', credentials);
};

export const registerUser = (userData) => {
  return api.post('/users/register/', userData);
};

export const getUserProfile = () => {
  return api.get('/users/profile/');
};

export const updateUserProfile = (data) => {
  return api.put('/users/profile/', data);
};
