import pytest
from products import Product


def test_create_normal_product():
    """Test that creating a normal product works"""

    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.get_quantity() == 100
    assert product.is_active()


def test_create_invalid_product():
    """Test that creating a product with invalid details invokes
    an exception"""

    with pytest.raises(Exception):
        Product("", price=-100, quantity=50)


def test_zero_quantity_product():
    """Test that a product becomes inactive when reaching 0 quantity"""

    product = Product("Bose QuietComfort Earbuds", price=250, quantity=0)
    assert not product.is_active()


def test_product_purchase():
    """Test that product purchase modifies the
    quantity and returns the right output"""

    product = Product("Google Pixel 7", price=500, quantity=250)
    total_price = product.buy(3)
    assert product.get_quantity() == 247
    assert total_price == 1500.0


def test_invalid_product_purchase():
    """Test that buying a larger quantity than exists invokes an exception"""

    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(150)


# Run the tests
pytest.main()
