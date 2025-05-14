from typing import Dict, Any
from datetime import datetime
from .product import Product

class Electronics(Product):
    """Class representing electronic products in the inventory."""
    
    def __init__(self, product_id: str, name: str, price: float, 
                 quantity_in_stock: int, warranty_years: int, brand: str):
        """
        Initialize a new electronic product.
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Name of the product
            price (float): Price of the product
            quantity_in_stock (int): Initial quantity in stock
            warranty_years (int): Number of years of warranty
            brand (str): Brand name of the product
        """
        super().__init__(product_id, name, price, quantity_in_stock)
        self._warranty_years = int(warranty_years)
        self._brand = brand
    
    @property
    def warranty_years(self) -> int:
        """Get the warranty period in years."""
        return self._warranty_years
    
    @property
    def brand(self) -> str:
        """Get the brand name."""
        return self._brand
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert electronic product to dictionary for serialization.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the product
        """
        base_dict = super().to_dict()
        base_dict.update({
            'warranty_years': self._warranty_years,
            'brand': self._brand
        })
        return base_dict
    
    def __str__(self) -> str:
        """Return a string representation of the electronic product."""
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Brand: {self._brand}\n"
                f"Warranty: {self._warranty_years} years") 