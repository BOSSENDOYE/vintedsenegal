import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const Header = () => {
  const { user, logout } = useContext(AuthContext);

  return (
    <header className="bg-white shadow p-4 flex justify-between items-center">
      <Link to="/" className="text-xl font-bold text-indigo-600">Vinted</Link>
      <nav className="flex items-center space-x-4">
        <Link to="/catalog" className="hover:text-indigo-500 transition-colors">Catalog</Link>
        
        {user ? (
          <>
            <Link 
              to="/create-listing" 
              className="hover:text-indigo-500 font-semibold bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 transition-colors"
            >
              Vendre
            </Link>
            <div className="relative group">
              <button className="flex items-center space-x-1 hover:text-indigo-500 transition-colors">
                <span>{user.username || user.email}</span>
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div className="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-50 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                <Link 
                  to="/dashboard" 
                  className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                >
                  Dashboard
                </Link>
                <Link 
                  to="/my-listings" 
                  className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                >
                  Mes Annonces
                </Link>
                <Link 
                  to="/messages" 
                  className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                >
                  Messages
                </Link>
                <Link 
                  to="/transactions" 
                  className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                >
                  Transactions
                </Link>
                <Link 
                  to="/settings" 
                  className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                >
                  Paramètres
                </Link>
                <hr className="my-1" />
                <button 
                  onClick={logout}
                  className="block w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-gray-100"
                >
                  Déconnexion
                </button>
              </div>
            </div>
          </>
        ) : (
          <>
            <Link to="/login" className="hover:text-indigo-500 transition-colors">Connexion</Link>
            <Link 
              to="/register" 
              className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition-colors"
            >
              Inscription
            </Link>
          </>
        )}
      </nav>
    </header>
  );
};

export default Header;
