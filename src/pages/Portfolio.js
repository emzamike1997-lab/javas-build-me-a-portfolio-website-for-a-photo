```javascript
import React, { useState, useEffect } from 'react';

function Portfolio() {
  const [images, setImages] = useState([]);

  useEffect(() => {
    const fetchImages = async () => {
      try {
        const response = await fetch('/api/images');
        const data = await response.json();
        setImages(data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchImages();
  }, []);

  return (
    <div className="portfolio">
      <h1>My portfolio</h1>
      <div className="image-grid">
        {images.map((image) => (
          <img key={image.id} src={image.url} alt={image.description} />
        ))}
      </div>
    </div>
  );
}

export default Portfolio;
```

###