import api from './api';

export const createPayment = (paymentData) => {
  return api.post('/payments/', paymentData);
};

export const getPaymentStatus = (paymentId) => {
  return api.get(`/payments/${paymentId}/status/`);
};
