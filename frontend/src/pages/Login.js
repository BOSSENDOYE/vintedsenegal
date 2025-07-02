import React from 'react';

const Login = () => {
  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Connexion</h1>
      <form>
        <label className="block mb-2">Email</label>
        <input type="email" className="border rounded w-full mb-4 p-2" />
        <label className="block mb-2">Mot de passe</label>
        <input type="password" className="border rounded w-full mb-4 p-2" />
        <button type="submit" className="bg-indigo-600 text-white px-4 py-2 rounded">
          Se connecter
        </button>
      </form>
    </div>
  );
};

export default Login;
