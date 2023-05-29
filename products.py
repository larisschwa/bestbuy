class Product:
    """Define functions for store actions"""

    def __init__(self, name, price, quantity):
        """Initialize a Product object.
            Args:
                name (str): The name of the product.
                price (float): The price of the product.
                quantity (int): The quantity of the product.

            Raises:
                ValueError: If the name is empty or the price/quantity
                is negative."""

        if not name or price < 0 or quantity < 0:
            raise ValueError(
                "Invalid input. Name cannot be empty and price/quantity "
                "cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Get the quantity of the product.
            Returns:
                int: The quantity of the product."""

        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity of the product.
            Args:
                quantity (int): The new quantity of the product."""

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Check if product is active.
            Returns: bool, True if active, False if not"""

        return self.active

    def activate(self):
        """Activate the product"""

        self.active = True

    def deactivate(self):
        """Deactivate the product"""

        self.active = False

    def show(self):
        """Get a str representation of the product
            Returns: str, the string representation"""

        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buy a certain quantity of the product
            Args: int, the quantity to buy
            Returns: float, total price of purchase
            Raises: ValueError, quantity is not a positive number or
            exceeds the available quantity"""

        if quantity <= 0:
            raise ValueError(
                "Invalid quantity. Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity available.")

        self.quantity -= quantity
        return self.price * quantity

    def __str__(self):
        """Get a str representation of the product
            Returns: str representation"""
        return self.name
