from typing import Dict, Any
from .product import Product

class Clothing(Product):
    """Class representing clothing products in the inventory."""
    
    def __init__(self, product_id: str, name: str, price: float, 
                 quantity_in_stock: int, size: str, material: str):
        """
        Initialize a new clothing product.
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Name of the product
            price (float): Price of the product
            quantity_in_stock (int): Initial quantity in stock
            size (str): Size of the clothing item
            material (str): Material of the clothing item
        """
        super().__init__(product_id, name, price, quantity_in_stock)
        self._size = size
        self._material = material
    
    @property
    def size(self) -> str:
        """Get the size of the clothing item."""
        return self._size
    
    @property
    def material(self) -> str:
        """Get the material of the clothing item."""
        return self._material
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert clothing product to dictionary for serialization.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the product
        """
        base_dict = super().to_dict()
        base_dict.update({
            'size': self._size,
            'material': self._material
        })
        return base_dict
    
    def __str__(self) -> str:
        """Return a string representation of the clothing product."""
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Size: {self._size}\n"
                f"Material: {self._material}") 