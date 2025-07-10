import React, { useContext, useState } from 'react';
import CreateListing from '../components/CreateListing';
import Notification from '../components/Notification';
import { createListing } from '../services/listingService';
import { useNavigate, Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const CreateListingPage = () => {
  const navigate = useNavigate();
  const { user } = useContext(AuthContext);
  const [notification, setNotification] = useState(null);

  const handleCreateListing = async (listingData) => {
    try {
      await createListing(listingData);
      setNotification({
        message: '🎉 Annonce créée avec succès ! Redirection vers votre dashboard...',
        type: 'success'
      });
      
      // Redirection après 2 secondes pour laisser le temps de voir la notification
      setTimeout(() => {
        navigate('/dashboard');
      }, 2000);
    } catch (error) {
      console.error('Erreur lors de la création de l\'annonce', error);
      setNotification({
        message: '❌ Erreur lors de la création de l\'annonce. Veuillez réessayer.',
        type: 'error'
      });
    }
  };

  if (!user) {
    return (
      <div className="p-4 max-w-md mx-auto text-center">
        <p className="mb-4">Vous devez être connecté pour créer une annonce.</p>
        <div className="space-x-4">
          <Link
            to="/register"
            className="inline-block bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
          >
            Inscrire
          </Link>
          <Link
            to="/login"
            className="inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Connexion
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="p-4">
      {notification && (
        <Notification
          message={notification.message}
          type={notification.type}
          onClose={() => setNotification(null)}
          autoClose={true}
          duration={3000}
        />
      )}
      <CreateListing onSubmit={handleCreateListing} />
    </div>
  );
};

export default CreateListingPage;
