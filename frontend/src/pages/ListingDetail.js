import React from 'react';
import { useParams } from 'react-router-dom';

const ListingDetail = () => {
  const { id } = useParams();

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Détail de l'annonce {id}</h1>
      <p>Informations détaillées sur l'annonce sélectionnée.</p>
    </div>
  );
};

export default ListingDetail;
