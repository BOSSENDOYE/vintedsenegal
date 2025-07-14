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
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { login } = useContext(AuthContext);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);
    
    // Validation côté client
    if (password !== password2) {
      setError('Les mots de passe ne correspondent pas.');
      setLoading(false);
      return;
    }
    
    if (password.length < 8) {
      setError('Le mot de passe doit contenir au moins 8 caractères.');
      setLoading(false);
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
        console.log('Inscription réussie:', response.data);
        
        // Si l'inscription retourne des tokens, les utiliser directement
        if (response.data.access && response.data.refresh) {
          const success = await login({ 
            access: response.data.access, 
            refresh: response.data.refresh 
          });
          if (success) {
            navigate('/dashboard');
            return;
          }
        }
        
        // Sinon, essayer de se connecter avec username/password
        const success = await login({ username, password });
        if (success) {
          navigate('/dashboard');
        } else {
          setError('Inscription réussie mais erreur lors de la connexion automatique.');
        }
      }
    } catch (err) {
      console.error('Registration error:', err);
      
      if (err.response && err.response.data) {
        // Gérer les erreurs de validation du backend
        if (typeof err.response.data === 'object') {
          const messages = Object.entries(err.response.data)
            .map(([field, msgs]) => {
              if (Array.isArray(msgs)) {
                return `${field}: ${msgs.join(', ')}`;
              }
              return `${field}: ${msgs}`;
            })
            .join(' ');
          setError(`Erreur de validation : ${messages}`);
        } else {
          setError(`Erreur : ${err.response.data}`);
        }
      } else if (err.message) {
        setError(`Erreur de connexion : ${err.message}`);
      } else {
        setError('Erreur lors de l\'inscription. Veuillez vérifier vos informations.');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Créer un compte</h1>
      {error && <p className="text-red-600 mb-4">{error}</p>}
      <form onSubmit={handleSubmit}>
        <label htmlFor="username" className="block mb-2">Nom d'utilisateur *</label>
        <input
          id="username"
          type="text"
          required
          className="border rounded w-full mb-4 p-2"
          placeholder="Votre nom d'utilisateur"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <label htmlFor="email" className="block mb-2">Email *</label>
        <input
          id="email"
          type="email"
          required
          className="border rounded w-full mb-4 p-2"
          placeholder="votre@email.com"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <label htmlFor="firstName" className="block mb-2">Prénom</label>
        <input
          id="firstName"
          type="text"
          className="border rounded w-full mb-4 p-2"
          placeholder="Prénom"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
        <label htmlFor="lastName" className="block mb-2">Nom</label>
        <input
          id="lastName"
          type="text"
          className="border rounded w-full mb-4 p-2"
          placeholder="Nom"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        />
        <label htmlFor="password" className="block mb-2">Mot de passe *</label>
        <input
          id="password"
          type="password"
          required
          className="border rounded w-full mb-4 p-2"
          placeholder="Au moins 8 caractères"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <label htmlFor="password2" className="block mb-2">Confirmer le mot de passe *</label>
        <input
          id="password2"
          type="password"
          required
          className="border rounded w-full mb-4 p-2"
          placeholder="Répétez votre mot de passe"
          value={password2}
          onChange={(e) => setPassword2(e.target.value)}
        />
        <button
          type="submit"
          disabled={loading}
          className={`w-full text-white px-4 py-2 rounded ${
            loading
              ? 'bg-gray-400 cursor-not-allowed'
              : 'bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'
          }`}
        >
          {loading ? 'Inscription en cours...' : 'S\'inscrire'}
        </button>
      </form>
      <div className="text-center mt-4">
        <span className="text-sm text-gray-600">Déjà inscrit ? </span>
        <a href="/login" className="font-medium text-indigo-600 hover:text-indigo-500">
          Se connecter
        </a>
      </div>
    </div>
  );
};

export default Register;
