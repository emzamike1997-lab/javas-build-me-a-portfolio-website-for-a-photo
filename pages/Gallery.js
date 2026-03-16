```javascript
import React, { useState, useEffect } from 'react';

function Gallery() {
  const [photos, setPhotos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://api.example.com/photos')
      .then(response => response.json())
      .then(data => {
        setPhotos(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <div>
      <h1>Gallery</h1>
      <div className="photo-grid">
        {photos.map(photo => (
          <img src={photo.url} alt={photo.title} key={photo.id} />
        ))}
      </div>
    </div>
  );
}

export default Gallery;
```

####