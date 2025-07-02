import api from './api';

export const getConversations = () => {
  return api.get('/conversations/');
};

export const getMessages = (conversationId) => {
  return api.get(`/conversations/${conversationId}/`);
};

export const sendMessage = (messageData) => {
  return api.post('/messages/create/', messageData);
};
