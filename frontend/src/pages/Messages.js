import React, { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import api from '../services/api';

const Messages = () => {
  const [searchParams] = useSearchParams();
  const vendeurId = searchParams.get('vendeur');
  const [message, setMessage] = useState('');
  const [sent, setSent] = useState(false);
  const [conversation, setConversation] = useState(null);
  const [loading, setLoading] = useState(true);

  // Charger la conversation entre l'utilisateur connecté et le vendeur ciblé
  useEffect(() => {
    const fetchConversation = async () => {
      setLoading(true);
      setConversation(null);
      if (!vendeurId) {
        setLoading(false);
        return;
      }
      try {
        // Récupérer toutes les conversations de l'utilisateur connecté
        const response = await api.get('/messaging/conversations/');
        // Chercher la conversation avec le vendeur ciblé
        const conv = response.data.find(c =>
          c.participants && c.participants.includes(Number(vendeurId))
        );
        setConversation(conv || null);
      } catch {
        setConversation(null);
      } finally {
        setLoading(false);
      }
    };
    fetchConversation();
  }, [vendeurId, sent]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!vendeurId || !message) return;
    try {
      await api.post('/messaging/messages/send/', {
        recipient_id: Number(vendeurId),
        content: message,
      });
      setSent(true);
      setMessage('');
      setTimeout(() => setSent(false), 2000);
    } catch (err) {
      if (err.response) {
        alert('Erreur lors de l\'envoi du message : ' + JSON.stringify(err.response.data));
      } else {
        alert("Erreur lors de l'envoi du message.");
      }
    }
  };

  if (!vendeurId) {
    return (
      <div className="p-4 max-w-xl mx-auto">
        <h1 className="text-2xl font-bold mb-4">Messages</h1>
        <p className="mb-4 text-gray-600">Sélectionnez une conversation pour discuter avec un utilisateur.</p>
      </div>
    );
  }

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Messagerie privée</h1>
      <p className="mb-4 text-gray-600">Espace de discussion entre vous et l'utilisateur #{vendeurId}.</p>
      {/* Historique des messages */}
      {loading ? (
        <div>Chargement de la conversation...</div>
      ) : conversation && conversation.messages && conversation.messages.length > 0 ? (
        <div className="mb-6 bg-gray-50 rounded p-4 max-h-80 overflow-y-auto">
          {conversation.messages.map(msg => (
            <div key={msg.id} className={`mb-2 p-2 rounded ${msg.sender === vendeurId ? 'bg-green-100 text-right' : 'bg-blue-100 text-left'}`}>
              <div className="text-sm">{msg.content}</div>
              <div className="text-xs text-gray-500">{new Date(msg.timestamp).toLocaleString()}</div>
            </div>
          ))}
        </div>
      ) : (
        <div className="mb-6 text-gray-500">Aucun message pour le moment.</div>
      )}
      {/* Formulaire d'envoi */}
      <form onSubmit={handleSend} className="mb-6">
        <label className="block mb-2 font-semibold">Envoyer un message à l'utilisateur #{vendeurId}</label>
        <textarea
          className="w-full border rounded p-2 mb-2"
          value={message}
          onChange={e => setMessage(e.target.value)}
          placeholder="Votre message..."
          required
        />
        <button
          type="submit"
          className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          Envoyer
        </button>
        {sent && (
          <div className="mt-2 text-green-600">Message envoyé !</div>
        )}
      </form>
    </div>
  );
};

export default Messages;
