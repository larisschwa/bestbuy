from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentageDiscountPromotion(Promotion):
    """Promotion class for percentage discount."""

    def __init__(self, name, discount_percentage):
        super().__init__(name)
        self.discount_percentage = discount_percentage

    def apply_promotion(self, product, quantity):
        discounted_price = product.price * (1 - self.discount_percentage / 100)
        return discounted_price * quantity


class SecondItemHalfPricePromotion(Promotion):
    """Promotion class for second item at half price."""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity % 2 == 0:
            discounted_price = (product.price * 1.5) * (quantity / 2)
        else:
            discounted_price = (product.price * 1.5) * (
                        quantity // 2) + product.price
        return discounted_price


class Buy2Get1FreePromotion(Promotion):
    """Promotion class for buy 2, get 1 free."""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        discounted_quantity = quantity - quantity // 3
        discounted_price = product.price * discounted_quantity
        return discounted_price

