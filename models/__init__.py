"""
Models package for the inventory management system.
Contains the base Product class and its subclasses.
"""

from .product import Product
from .electronics import Electronics
from .grocery import Grocery
from .clothing import Clothing
from .inventory import Inventory

__all__ = ['Product', 'Electronics', 'Grocery', 'Clothing', 'Inventory'] 