import React from 'react';

const Notification = ({ message, type }) => {
  if (!message) return null;

  const bgColor = type === 'error' ? 'bg-red-500' : 'bg-green-500';

  return (
    <div className={`${bgColor} text-white p-3 rounded mb-4`}>
      {message}
    </div>
  );
};

export default Notification;
