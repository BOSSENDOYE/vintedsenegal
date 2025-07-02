import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="bg-white shadow p-4 flex justify-between items-center">
      <Link to="/" className="text-xl font-bold text-indigo-600">Vinted</Link>
      <nav>
        <Link to="/catalog" className="mr-4 hover:text-indigo-500">Catalog</Link>
        <Link to="/create-listing" className="mr-4 hover:text-indigo-500 font-semibold bg-indigo-600 text-white px-3 py-1 rounded">
          Vendre
        </Link>
        <Link to="/login" className="hover:text-indigo-500">Login</Link>
      </nav>
    </header>
  );
};

export default Header;
