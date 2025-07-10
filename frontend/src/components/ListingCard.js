import React from 'react';
import { Link } from 'react-router-dom';
import { Calendar, User, Tag } from 'lucide-react';

const ListingCard = ({ listing }) => {
  // Fonction pour formater le prix
  const formatPrice = (price) => {
    if (!price) return 'Prix non défini';
    return new Intl.NumberFormat('fr-FR', {
      style: 'currency',
      currency: 'XOF',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(price);
  };

  // Fonction pour formater la date
  const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('fr-FR', {
      day: 'numeric',
      month: 'short',
      year: 'numeric'
    });
  };

  // Récupérer la première image
  const getFirstImage = () => {
    if (listing.photos && listing.photos.length > 0) {
      // Utiliser image_url si disponible, sinon image
      return listing.photos[0].image_url || listing.photos[0].image;
    }
    // Image par défaut si aucune photo
    return 'https://via.placeholder.com/300x200?text=Photo+non+disponible';
  };

  // Tronquer le titre si trop long
  const truncateTitle = (title, maxLength = 50) => {
    if (!title) return 'Sans titre';
    return title.length > maxLength ? title.substring(0, maxLength) + '...' : title;
  };

  // Tronquer la description si trop longue
  const truncateDescription = (description, maxLength = 100) => {
    if (!description) return 'Aucune description';
    return description.length > maxLength ? description.substring(0, maxLength) + '...' : description;
  };

  return (
    <div className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 overflow-hidden">
      {/* Image */}
      <div className="relative h-48 bg-gray-200">
        <img 
          src={getFirstImage()} 
          alt={listing.title || 'Annonce'} 
          className="w-full h-full object-cover"
          onError={(e) => {
            e.target.src = 'https://via.placeholder.com/300x200?text=Photo+non+disponible';
          }}
        />
        {/* Badge catégorie */}
        {listing.category && (
          <div className="absolute top-2 left-2 bg-green-600 text-white px-2 py-1 rounded-full text-xs font-medium">
            {listing.category}
          </div>
        )}
      </div>

      {/* Contenu */}
      <div className="p-4">
        {/* Titre */}
        <h3 className="text-lg font-semibold text-gray-900 mb-2 line-clamp-2">
          {truncateTitle(listing.title)}
        </h3>

        {/* Description */}
        <p className="text-gray-600 text-sm mb-3 line-clamp-2">
          {truncateDescription(listing.description)}
        </p>

        {/* Prix */}
        <div className="text-xl font-bold text-green-600 mb-3">
          {formatPrice(listing.price)}
        </div>

        {/* Informations supplémentaires */}
        <div className="space-y-1 text-xs text-gray-500 mb-4">
          {listing.seller && (
            <div className="flex items-center gap-1">
              <User size={12} />
              <span>{listing.seller}</span>
            </div>
          )}
          {listing.created_at && (
            <div className="flex items-center gap-1">
              <Calendar size={12} />
              <span>Publié le {formatDate(listing.created_at)}</span>
            </div>
          )}
          {listing.category && (
            <div className="flex items-center gap-1">
              <Tag size={12} />
              <span>{listing.category}</span>
            </div>
          )}
        </div>

        {/* Bouton Voir détails */}
        <Link 
          to={`/listing/${listing.id}`} 
          className="block w-full bg-green-600 text-white text-center py-2 px-4 rounded-md hover:bg-green-700 transition-colors duration-200 font-medium"
        >
          Voir les détails
        </Link>
      </div>
    </div>
  );
};

export default ListingCard;
