import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { registerUser } from '../services/userService';
import { AuthContext } from '../context/AuthContext';

const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [password, setPassword] = useState('');
  const [password2, setPassword2] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();
  const { login } = useContext(AuthContext);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    if (password !== password2) {
      setError('Les mots de passe ne correspondent pas.');
      return;
    }
    try {
      const response = await registerUser({
        username,
        email,
        first_name: firstName,
        last_name: lastName,
        password,
        password2,
      });
      if (response && response.data) {
        // Automatically log in the user after registration
        // Instead of passing response.data directly, call login with username and password
        const success = await login({ username, password });
        if (success) {
          navigate('/dashboard');
        } else {
          setError('Erreur lors de la connexion après inscription.');
        }
      }
    } catch (err) {
      if (err.response && err.response.data) {
        // Show detailed backend error messages
        const messages = Object.entries(err.response.data)
          .map(([field, msgs]) => `${field}: ${msgs.join(' ')}`)
          .join(' ');
        setError(`Erreur lors de l'inscription : ${messages}`);
      } else {
        setError('Erreur lors de l\'inscription. Veuillez vérifier vos informations.');
      }
      console.error('Registration error:', err);
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Inscription</h1>
      {error && <p className="text-red-600 mb-4">{error}</p>}
      <form onSubmit={handleSubmit}>
        <label className="block mb-2">Nom d'utilisateur</label>
        <input
          type="text"
          className="border rounded w-full mb-4 p-2"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <label className="block mb-2">Email</label>
        <input
          type="email"
          className="border rounded w-full mb-4 p-2"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <label className="block mb-2">Prénom</label>
        <input
          type="text"
          className="border rounded w-full mb-4 p-2"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
        <label className="block mb-2">Nom</label>
        <input
          type="text"
          className="border rounded w-full mb-4 p-2"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        />
        <label className="block mb-2">Mot de passe</label>
        <input
          type="password"
          className="border rounded w-full mb-4 p-2"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <label className="block mb-2">Confirmer le mot de passe</label>
        <input
          type="password"
          className="border rounded w-full mb-4 p-2"
          value={password2}
          onChange={(e) => setPassword2(e.target.value)}
          required
        />
        <button type="submit" className="bg-indigo-600 text-white px-4 py-2 rounded">
          S'inscrire
        </button>
      </form>
      <div className="mt-4 text-center">
        <span>Déjà inscrit ? </span>
        <a href="/login" className="text-indigo-600 hover:underline">Se connecter</a>
      </div>
    </div>
  );
};

export default Register;
