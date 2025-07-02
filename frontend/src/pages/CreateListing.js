import React from 'react';
import CreateListing from '../components/CreateListing';
import { createListing } from '../services/listingService';
import { useNavigate } from 'react-router-dom';

const CreateListingPage = () => {
  const navigate = useNavigate();

  const handleCreateListing = async (listingData) => {
    try {
      await createListing(listingData);
      alert('Annonce créée avec succès');
      navigate('/my-listings');
    } catch (error) {
      console.error('Erreur lors de la création de l\'annonce', error);
      alert('Erreur lors de la création de l\'annonce');
    }
  };

  return (
    <div className="p-4">
      <CreateListing onSubmit={handleCreateListing} />
    </div>
  );
};

export default CreateListingPage;
