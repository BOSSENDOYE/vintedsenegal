import React, { useEffect, useState } from 'react';
import api from '../services/api';

const Settings = () => {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await api.get('/users/profile/');
        setProfile(response.data);
      } catch {
        setProfile(null);
      } finally {
        setLoading(false);
      }
    };
    fetchProfile();
  }, []);

  if (loading) return <div>Chargement du profil...</div>;

  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Paramètres du compte</h1>
      {profile ? (
        <div className="space-y-2">
          <div><strong>Nom d'utilisateur :</strong> {profile.username}</div>
          <div><strong>Email :</strong> {profile.email}</div>
          <div><strong>Prénom :</strong> {profile.first_name}</div>
          <div><strong>Nom :</strong> {profile.last_name}</div>
          {/* Ajoute d'autres champs si besoin */}
        </div>
      ) : (
        <p>Impossible de charger le profil utilisateur.</p>
      )}
    </div>
  );
};

export default Settings;
