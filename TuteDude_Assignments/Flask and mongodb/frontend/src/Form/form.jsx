import React, { useState } from 'react';
import axios from 'axios';

function Form() {
  const [form, setForm] = useState({ name: '', email: '' });
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post(
        'http://127.0.0.1:5000/api/submit',
        form
      );

      if (res.data.success) {
        window.location.href = '/success';
      }

    } catch (err) {
      setError(err.response?.data?.error || "Something went wrong");
    }
  };

  return (
    <div>
      <h2>Submit Form</h2>

      {error && <p style={{color: 'red'}}>{error}</p>}

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name"
          onChange={(e) => setForm({...form, name: e.target.value})}
        /><br/>

        <input
          type="email"
          placeholder="Email"
          onChange={(e) => setForm({...form, email: e.target.value})}
        /><br/>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Form;