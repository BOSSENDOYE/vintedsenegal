import React, { useEffect, useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import ListingCard from '../components/ListingCard';
import CategoryFilter from '../components/CategoryFilter';
import SearchBar from '../components/SearchBar';
import { getListings } from '../services/listingService';
import { Search, ShoppingBag, TrendingUp, Users, Shield, Smartphone } from 'lucide-react';
import { AuthContext } from '../context/AuthContext';

const Home = () => {
  const [listings, setListings] = useState([]);
  const [filteredListings, setFilteredListings] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [selectedSubcategory, setSelectedSubcategory] = useState('');
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const navigate = useNavigate();
  const { user } = useContext(AuthContext);

  useEffect(() => {
    fetchListings();
  }, []);

  const fetchListings = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await getListings();
      setListings(response.data);
      setFilteredListings(response.data);
    } catch (error) {
      console.error('Erreur lors du chargement des annonces', error);
      setError('Erreur lors du chargement des annonces');
    } finally {
      setLoading(false);
    }
  };

  const handleCategorySelect = (category, subcategory = '') => {
    setSelectedCategory(category);
    setSelectedSubcategory(subcategory);
    filterListings(category, subcategory, searchQuery);
  };

  const handleSearch = (query) => {
    setSearchQuery(query);
    filterListings(selectedCategory, selectedSubcategory, query);
  };

  const filterListings = (category, subcategory, query) => {
    let filtered = listings;
    
    if (category && category !== 'Voir tout') {
      filtered = filtered.filter(listing => 
        listing.category && listing.category.toLowerCase() === category.toLowerCase()
      );
    }
    
    if (subcategory && subcategory !== 'Voir tout' && subcategory !== 'Autre') {
      filtered = filtered.filter(listing => 
        listing.subcategory && listing.subcategory.toLowerCase() === subcategory.toLowerCase()
      );
    }
    
    if (query) {
      filtered = filtered.filter(listing =>
        listing.title.toLowerCase().includes(query.toLowerCase()) ||
        (listing.description && listing.description.toLowerCase().includes(query.toLowerCase()))
      );
    }
    
    setFilteredListings(filtered);
  };

  const clearFilters = () => {
    setSelectedCategory('');
    setSelectedSubcategory('');
    setSearchQuery('');
    setFilteredListings(listings);
  };

  const navigateToCatalog = () => {
    navigate('/catalog');
  };

  // Statistiques factices pour l'affichage (à remplacer par de vraies données)
  const stats = {
    totalListings: listings.length,
    activeUsers: '2,500+',
    successfulSales: '15,000+'
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <div className="bg-gradient-to-r from-green-600 to-blue-600 text-white">
        <div className="max-w-7xl mx-auto px-4 py-16">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              Bienvenue sur <span className="text-yellow-300">Vinted</span> Dakar
            </h1>
            <p className="text-xl md:text-2xl mb-8 max-w-3xl mx-auto">
              La plateforme de référence au Sénégal pour vendre, acheter et échanger 
              vos articles d'occasion. Mode, beauté, accessoires... tout y est !
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button
                onClick={navigateToCatalog}
                className="bg-white text-green-600 px-8 py-4 rounded-lg font-semibold text-lg hover:bg-gray-100 transition-colors flex items-center justify-center gap-2"
              >
                <Search size={24} />
                Découvrir le catalogue
              </button>
              <button
                onClick={() => {
                  if (user) {
                    navigate('/create-listing');
                  } else {
                    navigate('/register');
                  }
                }}
                className="bg-yellow-400 text-gray-900 px-8 py-4 rounded-lg font-semibold text-lg hover:bg-yellow-300 transition-colors flex items-center justify-center gap-2"
              >
                <ShoppingBag size={24} />
                Vendre maintenant
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Stats Section */}
      <div className="bg-white py-12">
        <div className="max-w-7xl mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
            <div className="p-6">
              <div className="text-3xl font-bold text-green-600 mb-2">{stats.totalListings}+</div>
              <div className="text-gray-600">Articles disponibles</div>
            </div>
            <div className="p-6">
              <div className="text-3xl font-bold text-blue-600 mb-2">{stats.activeUsers}</div>
              <div className="text-gray-600">Utilisateurs actifs</div>
            </div>
            <div className="p-6">
              <div className="text-3xl font-bold text-yellow-600 mb-2">{stats.successfulSales}</div>
              <div className="text-gray-600">Ventes réussies</div>
            </div>
          </div>
        </div>
      </div>

      {/* Quick Search Section */}
      <div className="max-w-7xl mx-auto px-4 py-12">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">
            Trouvez ce que vous cherchez
          </h2>
          <p className="text-gray-600 text-lg max-w-2xl mx-auto">
            Utilisez nos filtres avancés pour trouver l'article parfait parmi des milliers d'annonces
          </p>
        </div>

        <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
          <SearchBar onSearch={handleSearch} placeholder="Rechercher des articles..." />
          <div className="mt-6">
            <CategoryFilter 
              selectedCategory={selectedCategory}
              selectedSubcategory={selectedSubcategory}
              onSelectCategory={handleCategorySelect}
            />
          </div>
          
          {(selectedCategory || searchQuery) && (
            <div className="mt-4 flex flex-wrap gap-2">
              {selectedCategory && (
                <span className="bg-green-100 text-green-800 px-3 py-1 rounded-full text-sm">
                  {selectedCategory}
                  {selectedSubcategory && ` > ${selectedSubcategory}`}
                </span>
              )}
              {searchQuery && (
                <span className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm">
                  "{searchQuery}"
                </span>
              )}
              <button
                onClick={clearFilters}
                className="text-red-600 hover:text-red-800 text-sm font-medium"
              >
                Effacer les filtres
              </button>
            </div>
          )}
        </div>

        {/* Loading State */}
        {loading && (
          <div className="text-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-4 border-green-500 border-t-transparent mx-auto mb-4"></div>
            <p className="text-gray-600">Chargement des annonces...</p>
          </div>
        )}

        {/* Error State */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
            <p className="text-red-600">{error}</p>
            <button
              onClick={fetchListings}
              className="mt-2 text-red-700 hover:text-red-900 font-medium"
            >
              Réessayer
            </button>
          </div>
        )}

        {/* Results Section */}
        <div className="mb-6">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-xl font-semibold text-gray-900">
              {filteredListings.length > 0 
                ? `${filteredListings.length} article${filteredListings.length > 1 ? 's' : ''} trouvé${filteredListings.length > 1 ? 's' : ''}`
                : 'Aucun article trouvé'
              }
            </h3>
            {filteredListings.length > 0 && (
              <button
                onClick={navigateToCatalog}
                className="text-green-600 hover:text-green-800 font-medium"
              >
                Voir tout le catalogue →
              </button>
            )}
          </div>

          {/* Listings Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {filteredListings.slice(0, 8).map((listing) => (
              <ListingCard key={listing.id} listing={listing} />
            ))}
          </div>

          {filteredListings.length === 0 && !loading && (
            <div className="text-center py-12">
              <ShoppingBag size={48} className="mx-auto text-gray-400 mb-4" />
              <p className="text-gray-600 text-lg mb-4">
                Aucune annonce ne correspond à vos critères
              </p>
              <button
                onClick={clearFilters}
                className="bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700 transition-colors"
              >
                Voir toutes les annonces
              </button>
            </div>
          )}
        </div>
      </div>

      {/* Features Section */}
      <div className="bg-gray-100 py-16">
        <div className="max-w-7xl mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              Pourquoi choisir Vinted Dakar ?
            </h2>
            <p className="text-gray-600 text-lg">
              Une expérience adaptée aux besoins du marché sénégalais
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center p-6">
              <div className="bg-green-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <Smartphone className="text-green-600" size={32} />
              </div>
              <h3 className="text-xl font-semibold mb-2">Interface Mobile</h3>
              <p className="text-gray-600">
                Optimisée pour les connexions 3G/4G et les smartphones
              </p>
            </div>

            <div className="text-center p-6">
              <div className="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <Shield className="text-blue-600" size={32} />
              </div>
              <h3 className="text-xl font-semibold mb-2">Transactions Sécurisées</h3>
              <p className="text-gray-600">
                Système de paiement adapté au contexte local sénégalais
              </p>
            </div>

            <div className="text-center p-6">
              <div className="bg-yellow-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <Users className="text-yellow-600" size={32} />
              </div>
              <h3 className="text-xl font-semibold mb-2">Communauté Locale</h3>
              <p className="text-gray-600">
                Connectez-vous avec des vendeurs et acheteurs de Dakar
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="bg-green-600 py-16">
        <div className="max-w-4xl mx-auto text-center px-4">
          <h2 className="text-3xl font-bold text-white mb-4">
            Prêt à commencer ?
          </h2>
          <p className="text-green-100 text-lg mb-8">
            Rejoignez des milliers d'utilisateurs qui font déjà confiance à Vinted Dakar
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button
              onClick={() => navigate('/register')}
              className="bg-white text-green-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors"
            >
              Créer un compte
            </button>
            <button
              onClick={navigateToCatalog}
              className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white hover:text-green-600 transition-colors"
            >
              Explorer sans compte
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;