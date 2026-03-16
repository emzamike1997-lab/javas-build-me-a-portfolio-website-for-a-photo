```javascript
import React from 'react';

function Home() {
  return (
    <div>
      <h1>Welcome to my portfolio website</h1>
      <p>I'm a photographer with a passion for capturing beautiful moments.</p>
      <div className="hero-section">
        <img src="hero-image.jpg" alt="Hero Image" />
      </div>
      <div className="featured-photos">
        <h2>Featured Photos</h2>
        <div className="photo-grid">
          <img src="photo1.jpg" alt="Photo 1" />
          <img src="photo2.jpg" alt="Photo 2" />
          <img src="photo3.jpg" alt="Photo 3" />
        </div>
      </div>
    </div>
  );
}

export default Home;
```

####