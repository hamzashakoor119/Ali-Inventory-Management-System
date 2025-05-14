from abc import ABC, abstractmethod
from typing import Dict, Any
from datetime import datetime
from exceptions.custom_exceptions import InsufficientStockError

class Product(ABC):
    """Abstract base class for all products in the inventory system."""
    
    def __init__(self, product_id: str, name: str, price: float, quantity_in_stock: int):
        """
        Initialize a new product.
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Name of the product
            price (float): Price of the product
            quantity_in_stock (int): Initial quantity in stock
        """
        self._product_id = product_id
        self._name = name
        self._price = float(price)
        self._quantity_in_stock = int(quantity_in_stock)
        
    @property
    def product_id(self) -> str:
        """Get the product ID."""
        return self._product_id
    
    @property
    def name(self) -> str:
        """Get the product name."""
        return self._name
    
    @property
    def price(self) -> float:
        """Get the product price."""
        return self._price
    
    @price.setter
    def price(self, new_price: float) -> None:
        """Set a new price for the product."""
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = float(new_price)
    
    @property
    def quantity_in_stock(self) -> int:
        """Get the current quantity in stock."""
        return self._quantity_in_stock
    
    def restock(self, amount: int) -> None:
        """
        Add more items to stock.
        
        Args:
            amount (int): Number of items to add
            
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Restock amount cannot be negative")
        self._quantity_in_stock += amount
    
    def sell(self, quantity: int) -> float:
        """
        Sell a quantity of the product.
        
        Args:
            quantity (int): Number of items to sell
            
        Returns:
            float: Total value of the sale
            
        Raises:
            ValueError: If quantity is negative
            InsufficientStockError: If trying to sell more than available
        """
        if quantity < 0:
            raise ValueError("Sale quantity cannot be negative")
        if quantity > self._quantity_in_stock:
            raise InsufficientStockError(self._product_id, quantity, self._quantity_in_stock)
        
        self._quantity_in_stock -= quantity
        return self._price * quantity
    
    def get_total_value(self) -> float:
        """
        Calculate the total value of current stock.
        
        Returns:
            float: Total value (price * quantity)
        """
        return self._price * self._quantity_in_stock
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert product to dictionary for serialization.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the product
        """
        return {
            'product_id': self._product_id,
            'name': self._name,
            'price': self._price,
            'quantity_in_stock': self._quantity_in_stock,
            'type': self.__class__.__name__
        }
    
    @abstractmethod
    def __str__(self) -> str:
        """Return a string representation of the product."""
        return (f"Product ID: {self._product_id}\n"
                f"Name: {self._name}\n"
                f"Price: ${self._price:.2f}\n"
                f"Quantity in Stock: {self._quantity_in_stock}") 