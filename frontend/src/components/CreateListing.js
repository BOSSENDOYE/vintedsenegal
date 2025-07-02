import React, { useState } from 'react';

const CreateListing = ({ onSubmit }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [category, setCategory] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ title, description, price, category });
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto p-4 bg-white shadow rounded">
      <h2 className="text-xl font-bold mb-4">Créer une annonce</h2>
      <label className="block mb-2">Titre</label>
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="border rounded w-full mb-4 p-2"
        required
      />
      <label className="block mb-2">Description</label>
      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        className="border rounded w-full mb-4 p-2"
        rows="4"
        required
      />
      <label className="block mb-2">Prix</label>
      <input
        type="number"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
        className="border rounded w-full mb-4 p-2"
        required
      />
      <label className="block mb-2">Catégorie</label>
      <input
        type="text"
        value={category}
        onChange={(e) => setCategory(e.target.value)}
        className="border rounded w-full mb-4 p-2"
        required
      />
      <button type="submit" className="bg-indigo-600 text-white px-4 py-2 rounded">
        Publier
      </button>
    </form>
  );
};

export default CreateListing;
