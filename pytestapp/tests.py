import pytest
from . models import Product

# Create your tests here.
@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(name="Test Product", description="Test Product Description")
    assert product.name == "Test Product"
    assert product.description == "Test Product Description"