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

        if not name:
            raise Exception("Invalid product name")
        if price < 0:
            raise Exception("Invalid product price")
        if quantity < 0:
            raise Exception("Invalid product quantity")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.promotion = None

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
        if self.promotion is not None:
            return self.promotion.apply_promotion(self, quantity)
        else:
            self.quantity -= quantity
            return self.price * quantity

    def __str__(self):
        """Get a str representation of the product
            Returns: str representation"""

        return self.name

    def set_promotion(self, promotion):
        """Set the promotion for the product."""
        self.promotion = promotion

    def get_promotion(self):
        """Get the promotion for the product."""
        return self.promotion


class NonStockedProduct(Product):
    """Represents a non-stocked product in the store.

    Inherits from the Product class and sets the quantity to 0.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product."""

    def __init__(self, name, price):
        """Initializes a non-stocked product.

        Args:
            name (str): The name of the product.
            price (float): The price of the product."""

        super().__init__(name, price, 0)

    def show(self):
        """Returns a string representation of the non-stocked product.

        Returns:
            str: A string representing the non-stocked product."""

        return f"{self.name}, Price: {self.price}, Quantity: Non-stocked"


class LimitedProduct(Product):
    """Represents a limited product in the store.

    Inherits from the Product class and allows purchasing a limited quantity.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity_limit (int): The maximum quantity allowed for purchase."""

    def __init__(self, name, price, quantity_limit):
        """Initializes a limited product.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity_limit (int): The maximum quantity allowed for purchase."""

        super().__init__(name, price, 0)
        self.quantity_limit = quantity_limit

    def buy(self, quantity):
        """Buys a given quantity of the limited product.

        Overrides the buy method to check if the quantity exceeds
        the maximum limit.

        Args:
            quantity (int): The quantity to purchase.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity is invalid or
            exceeds the maximum limit."""

        if quantity <= 0:
            raise ValueError(
                "Invalid quantity. Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity available.")

        self.quantity -= quantity
        total_price = self.price * quantity
        return total_price

    def show(self):
        """Returns a string representation of the limited product.

        Overrides the show method to include the quantity limit.

        Returns:
            str: A string representing the limited product."""

        return f"{self.name}, Price: {self.price}, Quantity Limit: " \
               f"{self.quantity_limit}"
