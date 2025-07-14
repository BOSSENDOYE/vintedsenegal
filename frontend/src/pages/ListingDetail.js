import React, { useState, useEffect, useContext } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { getListingById } from '../services/listingService';
import { AuthContext } from '../context/AuthContext';
import { ArrowLeft, Calendar, User, Tag, MapPin, Phone, MessageCircle, Heart, Share2 } from 'lucide-react';

const ListingDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { user } = useContext(AuthContext);
  const [listing, setListing] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedImage, setSelectedImage] = useState(0);

  useEffect(() => {
    fetchListing();
  }, [id]);

  const fetchListing = async () => {
    try {
      setLoading(true);
      const response = await getListingById(id);
      setListing(response.data);
    } catch (error) {
      console.error('Erreur lors du chargement de l\'annonce', error);
      setError('Erreur lors du chargement de l\'annonce');
    } finally {
      setLoading(false);
    }
  };

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
      month: 'long',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  // Récupérer les images
  const getImages = () => {
    if (listing?.photos && listing.photos.length > 0) {
      return listing.photos.map(photo => photo.image_url || photo.image);
    }
    return ['https://via.placeholder.com/600x400?text=Photo+non+disponible'];
  };

  // Fonction utilitaire pour obtenir l'ID numérique du vendeur
  const getSellerId = () => {
    if (!listing) return '';
    if (typeof listing.seller === 'object' && listing.seller.id) return listing.seller.id;
    if (listing.seller_id) return listing.seller_id;
    if (!isNaN(Number(listing.seller))) return Number(listing.seller);
    return '';
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-4 border-green-500 border-t-transparent mx-auto mb-4"></div>
          <p className="text-gray-600">Chargement de l'annonce...</p>
        </div>
      </div>
    );
  }

  if (error || !listing) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600 mb-4">{error || 'Annonce non trouvée'}</p>
          <button
            onClick={() => navigate('/')}
            className="bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700"
          >
            Retour à l'accueil
          </button>
        </div>
      </div>
    );
  }

  const images = getImages();

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <button
              onClick={() => navigate(-1)}
              className="flex items-center gap-2 text-gray-600 hover:text-gray-900"
            >
              <ArrowLeft size={20} />
              Retour
            </button>
            <div className="flex items-center gap-4">
              <button className="flex items-center gap-2 text-gray-600 hover:text-gray-900">
                <Heart size={20} />
                Favoris
              </button>
              <button className="flex items-center gap-2 text-gray-600 hover:text-gray-900">
                <Share2 size={20} />
                Partager
              </button>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Images */}
          <div className="space-y-4">
            {/* Image principale */}
            <div className="bg-white rounded-lg shadow-md overflow-hidden">
              <img
                src={images[selectedImage]}
                alt={listing.title}
                className="w-full h-96 object-cover"
                onError={(e) => {
                  e.target.src = 'https://via.placeholder.com/600x400?text=Photo+non+disponible';
                }}
              />
            </div>

            {/* Miniatures */}
            {images.length > 1 && (
              <div className="grid grid-cols-5 gap-2">
                {images.map((image, index) => (
                  <button
                    key={index}
                    onClick={() => setSelectedImage(index)}
                    className={`bg-white rounded-lg shadow-md overflow-hidden border-2 ${
                      selectedImage === index ? 'border-green-500' : 'border-transparent'
                    }`}
                  >
                    <img
                      src={image}
                      alt={`${listing.title} ${index + 1}`}
                      className="w-full h-20 object-cover"
                      onError={(e) => {
                        e.target.src = 'https://via.placeholder.com/100x80?text=Photo';
                      }}
                    />
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Informations */}
          <div className="space-y-6">
            {/* Titre et prix */}
            <div className="bg-white rounded-lg shadow-md p-6">
              <h1 className="text-3xl font-bold text-gray-900 mb-4">{listing.title}</h1>
              <div className="text-3xl font-bold text-green-600 mb-4">
                {formatPrice(listing.price)}
              </div>
              
              {/* Badge catégorie */}
              {listing.category && (
                <div className="inline-block bg-green-100 text-green-800 px-3 py-1 rounded-full text-sm font-medium mb-4">
                  {listing.category}
                </div>
              )}
            </div>

            {/* Description */}
            <div className="bg-white rounded-lg shadow-md p-6">
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Description</h2>
              <p className="text-gray-700 leading-relaxed whitespace-pre-wrap">
                {listing.description}
              </p>
            </div>

            {/* Informations du vendeur */}
            <div className="bg-white rounded-lg shadow-md p-6">
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Informations du vendeur</h2>
              <div className="space-y-3">
                {listing.seller && (
                  <div className="flex items-center gap-3">
                    <User size={20} className="text-gray-500" />
                    <span className="text-gray-700">{listing.seller}</span>
                  </div>
                )}
                {listing.created_at && (
                  <div className="flex items-center gap-3">
                    <Calendar size={20} className="text-gray-500" />
                    <span className="text-gray-700">Publié le {formatDate(listing.created_at)}</span>
                  </div>
                )}
                {listing.category && (
                  <div className="flex items-center gap-3">
                    <Tag size={20} className="text-gray-500" />
                    <span className="text-gray-700">Catégorie: {listing.category}</span>
                  </div>
                )}
              </div>
            </div>

            {/* Actions */}
            <div className="bg-white rounded-lg shadow-md p-6">
              <div className="space-y-4">
                {user ? (
                  <>
                    <button
                      className="w-full bg-green-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-green-700 transition-colors flex items-center justify-center gap-2"
                      onClick={() => navigate(`/messages?vendeur=${getSellerId()}`)}
                    >
                      <MessageCircle size={20} />
                      Contacter le vendeur
                    </button>
                    <button className="w-full bg-blue-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-blue-700 transition-colors flex items-center justify-center gap-2">
                      <Phone size={20} />
                      Appeler le vendeur
                    </button>
                  </>
                ) : (
                  <div className="text-center space-y-4">
                    <p className="text-gray-600">Connectez-vous pour contacter le vendeur</p>
                    <div className="flex gap-4">
                      <Link
                        to="/login"
                        className="flex-1 bg-green-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-green-700 transition-colors text-center"
                      >
                        Se connecter
                      </Link>
                      <Link
                        to="/register"
                        className="flex-1 bg-blue-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-blue-700 transition-colors text-center"
                      >
                        S'inscrire
                      </Link>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ListingDetail;
