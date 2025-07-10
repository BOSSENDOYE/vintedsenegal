import api from './api';

export const getListings = (params) => {
  return api.get('/listings/', { params });
};

export const getListingById = (id) => {
  return api.get(`/listings/${id}/`);
};

export const createListing = (data) => {
  // Si c'est un FormData (avec images), ne pas ajouter de Content-Type
  if (data instanceof FormData) {
    return api.post('/listings/create/', data, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
  }
  // Sinon, utiliser JSON
  return api.post('/listings/create/', data);
};

export const updateListing = (id, data) => {
  return api.put(`/listings/${id}/update/`, data);
};

export const deleteListing = (id) => {
  return api.delete(`/listings/${id}/`);
};
