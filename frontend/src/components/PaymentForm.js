import React, { useState } from 'react';

const PaymentForm = ({ onPayment }) => {
  const [amount, setAmount] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (amount) {
      onPayment(amount);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto p-4 border rounded">
      <label className="block mb-2 font-semibold" htmlFor="amount">
        Montant à payer
      </label>
      <input
        type="number"
        id="amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        className="border rounded px-3 py-2 w-full mb-4"
        min="1"
        required
      />
      <button
        type="submit"
        className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700"
      >
        Payer
      </button>
    </form>
  );
};

export default PaymentForm;
