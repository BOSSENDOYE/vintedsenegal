import React from 'react';

const Contact = () => {
  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Contact</h1>
      <form>
        <label className="block mb-2">Nom</label>
        <input type="text" className="border rounded w-full mb-4 p-2" />
        <label className="block mb-2">Email</label>
        <input type="email" className="border rounded w-full mb-4 p-2" />
        <label className="block mb-2">Message</label>
        <textarea className="border rounded w-full mb-4 p-2" rows="4"></textarea>
        <button type="submit" className="bg-indigo-600 text-white px-4 py-2 rounded">
          Envoyer
        </button>
      </form>
    </div>
  );
};

export default Contact;
