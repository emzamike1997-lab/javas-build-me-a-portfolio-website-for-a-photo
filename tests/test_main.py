### Test Strategy
The test strategy for this project will involve a combination of unit tests and integration tests. Unit tests will focus on individual components of the website, such as the navigation menu, image gallery, and contact form. Integration tests will test how these components interact with each other and with the overall website.

### Unit Tests
Unit tests will be written using the Pytest framework.

=== test_navigation.py ===
```python
import pytest
from portfolio_website.navigation import Navigation

def test_navigation_init():
    nav = Navigation()
    assert nav.links == []

def test_navigation_add_link():
    nav = Navigation()
    nav.add_link("Home", "/")
    assert nav.links == [("Home", "/")]

def test_navigation_remove_link():
    nav = Navigation()
    nav.add_link("Home", "/")
    nav.remove_link("Home")
    assert nav.links == []
```

=== test_image_gallery.py ===
```python
import pytest
from portfolio_website.image_gallery import ImageGallery

def test_image_gallery_init():
    gallery = ImageGallery()
    assert gallery.images == []

def test_image_gallery_add_image():
    gallery = ImageGallery()
    gallery.add_image("image1.jpg", "Image 1")
    assert gallery.images == [("image1.jpg", "Image 1")]

def test_image_gallery_remove_image():
    gallery = ImageGallery()
    gallery.add_image("image1.jpg", "Image 1")
    gallery.remove_image("image1.jpg")
    assert gallery.images == []
```

=== test_contact_form.py ===
```python
import pytest
from portfolio_website.contact_form import ContactForm

def test_contact_form_init():
    form = ContactForm()
    assert form.fields == {}

def test_contact_form_add_field():
    form = ContactForm()
    form.add_field("name", "Name")
    assert form.fields == {"name": "Name"}

def test_contact_form_remove_field():
    form = ContactForm()
    form.add_field("name", "Name")
    form.remove_field("name")
    assert form.fields == {}
```

### Integration Tests
Integration tests will be written using the Pytest framework and the Selenium WebDriver.

=== test_website.py ===
```python
import pytest
from selenium import webdriver
from portfolio_website import app

@pytest.fixture
def browser():
    return webdriver.Chrome()

def test_homepage(browser):
    browser.get("http://localhost:5000")
    assert browser.title == "Photographer Portfolio"

def test_navigation(browser):
    browser.get("http://localhost:5000")
    nav = browser.find_element_by_id("nav")
    assert nav.is_displayed()

def test_image_gallery(browser):
    browser.get("http://localhost:5000/gallery")
    gallery = browser.find_element_by_id("gallery")
    assert gallery.is_displayed()

def test_contact_form(browser):
    browser.get("http://localhost:5000/contact")
    form = browser.find_element_by_id("contact-form")
    assert form.is_displayed()
```

### API Tests
API tests will be written using the Pytest framework and the Requests library.

=== test_api.py ===
```python
import pytest
import requests
from portfolio_website import app

def test_api_get_images():
    response = requests.get("http://localhost:5000/api/images")
    assert response.status_code == 200
    assert response.json() != []

def test_api_get_image():
    response = requests.get("http://localhost:5000/api/images/1")
    assert response.status_code == 200
    assert response.json() != {}

def test_api_post_contact():
    data = {"name": "John Doe", "email": "john@example.com", "message": "Hello"}
    response = requests.post("http://localhost:5000/api/contact", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Contact form submitted successfully"}
```

### Test Coverage
To ensure that all parts of the code are tested, we will use the Coverage.py library to measure test coverage.

=== test_coverage.py ===
```python
import coverage
import pytest

def test_coverage():
    cov = coverage.Coverage()
    cov.start()
    pytest.main(["-v", "tests/"])
    cov.stop()
    cov.save()
    cov.report()
```

Note: The above tests are just examples and may need to be modified to fit the specific requirements of your project. Additionally, you may need to install additional libraries or frameworks to run these tests.