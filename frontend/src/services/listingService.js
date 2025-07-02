import api from './api';

export const getListings = (params) => {
  return api.get('/listings/', { params });
};

export const getListingById = (id) => {
  return api.get(`/listings/${id}/`);
};

export const createListing = (data) => {
  return api.post('/listings/create/', data);
};

export const updateListing = (id, data) => {
  return api.put(`/listings/${id}/update/`, data);
};

export const deleteListing = (id) => {
  return api.delete(`/listings/${id}/`);
};
