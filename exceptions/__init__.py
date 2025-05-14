"""
Exceptions package for the inventory management system.
Contains custom exception classes for error handling.
"""

from .custom_exceptions import (
    InventoryError,
    InsufficientStockError,
    DuplicateProductError,
    ProductNotFoundError,
    InvalidProductDataError,
    InvalidProductTypeError
)

__all__ = [
    'InventoryError',
    'InsufficientStockError',
    'DuplicateProductError',
    'ProductNotFoundError',
    'InvalidProductDataError',
    'InvalidProductTypeError'
] 