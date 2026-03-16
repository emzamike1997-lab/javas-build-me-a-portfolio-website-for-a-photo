```javascript
import React, { useState } from 'react';

function Contact() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [sent, setSent] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = event => {
    event.preventDefault();
    fetch('https://api.example.com/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, message }),
    })
      .then(response => response.json())
      .then(data => {
        setSent(true);
      })
      .catch(error => {
        setError(error);
      });
  };

  return (
    <div>
      <h1>Contact</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" value={name} onChange={event => setName(event.target.value)} />
        </label>
        <label>
          Email:
          <input type="email" value={email} onChange={event => setEmail(event.target.value)} />
        </label>
        <label>
          Message:
          <textarea value={message} onChange={event => setMessage(event.target.value)} />
        </label>
        <button type="submit">Send</button>
      </form>
      {sent ? <p>Message sent successfully!</p> : null}
      {error ? <p>Error: {error.message}</p> : null}
    </div>
  );
}

export default Contact;
```

####