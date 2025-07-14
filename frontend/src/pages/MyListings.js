import React, { useEffect, useState } from 'react';
import api from '../services/api';
import ListingCard from '../components/ListingCard';

const MyListings = () => {
  const [listings, setListings] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchListings = async () => {
      try {
        const response = await api.get('/listings/seller/');
        setListings(response.data);
      } catch (error) {
        setListings([]);
      } finally {
        setLoading(false);
      }
    };
    fetchListings();
  }, []);

  const handleDelete = async (id) => {
    if (window.confirm('Voulez-vous vraiment supprimer cette annonce ?')) {
      try {
        await api.delete(`/listings/${id}/delete/`);
        setListings(listings.filter(listing => listing.id !== id));
      } catch (error) {
        alert("Erreur lors de la suppression de l'annonce.");
      }
    }
  };

  if (loading) return <div>Chargement...</div>;

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Mes annonces</h1>
      {listings.length === 0 ? (
        <p>Aucune annonce trouvée.</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {listings.map(listing => (
            <div key={listing.id} className="relative">
              <ListingCard listing={listing} />
              <button
                onClick={() => handleDelete(listing.id)}
                className="absolute top-2 right-2 bg-red-600 text-white px-2 py-1 rounded hover:bg-red-700"
              >
                Supprimer
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default MyListings;

