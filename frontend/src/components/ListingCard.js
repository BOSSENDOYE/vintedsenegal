import React from 'react';
import { Link } from 'react-router-dom';

const ListingCard = ({ listing }) => {
  return (
    <div className="border rounded shadow p-4">
      <img src={listing.image} alt={listing.title} className="w-full h-48 object-cover mb-2 rounded" />
      <h3 className="text-lg font-semibold">{listing.title}</h3>
      <p className="text-gray-600">{listing.price} €</p>
      <Link to={`/listing/${listing.id}`} className="text-indigo-600 hover:underline mt-2 block">
        Voir les détails
      </Link>
    </div>
  );
};

export default ListingCard;
