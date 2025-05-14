from typing import Dict, Any
from datetime import datetime
from dateutil.parser import parse
from .product import Product

class Grocery(Product):
    """Class representing grocery products in the inventory."""
    
    def __init__(self, product_id: str, name: str, price: float, 
                 quantity_in_stock: int, expiry_date: str):
        """
        Initialize a new grocery product.
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Name of the product
            price (float): Price of the product
            quantity_in_stock (int): Initial quantity in stock
            expiry_date (str): Expiry date in ISO format (YYYY-MM-DD)
        """
        super().__init__(product_id, name, price, quantity_in_stock)
        self._expiry_date = parse(expiry_date).date()
    
    @property
    def expiry_date(self) -> datetime.date:
        """Get the expiry date."""
        return self._expiry_date
    
    def is_expired(self) -> bool:
        """
        Check if the product has expired.
        
        Returns:
            bool: True if the product has expired, False otherwise
        """
        return datetime.now().date() > self._expiry_date
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert grocery product to dictionary for serialization.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the product
        """
        base_dict = super().to_dict()
        base_dict.update({
            'expiry_date': self._expiry_date.isoformat()
        })
        return base_dict
    
    def __str__(self) -> str:
        """Return a string representation of the grocery product."""
        base_str = super().__str__()
        expiry_status = "EXPIRED" if self.is_expired() else "Valid"
        return (f"{base_str}\n"
                f"Expiry Date: {self._expiry_date.isoformat()}\n"
                f"Status: {expiry_status}") 