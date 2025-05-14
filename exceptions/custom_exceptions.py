class InventoryError(Exception):
    """Base exception class for inventory-related errors."""
    pass

class InsufficientStockError(InventoryError):
    """Raised when trying to sell more items than available in stock."""
    def __init__(self, product_id: str, requested: int, available: int):
        self.product_id = product_id
        self.requested = requested
        self.available = available
        super().__init__(
            f"Insufficient stock for product {product_id}. "
            f"Requested: {requested}, Available: {available}"
        )

class DuplicateProductError(InventoryError):
    """Raised when trying to add a product with an ID that already exists."""
    def __init__(self, product_id: str):
        self.product_id = product_id
        super().__init__(f"Product with ID {product_id} already exists in inventory")

class ProductNotFoundError(InventoryError):
    """Raised when a product cannot be found in the inventory."""
    def __init__(self, product_id: str):
        self.product_id = product_id
        super().__init__(f"Product with ID {product_id} not found in inventory")

class InvalidProductDataError(InventoryError):
    """Raised when trying to load invalid product data from file."""
    def __init__(self, message: str):
        super().__init__(f"Invalid product data: {message}")

class InvalidProductTypeError(InventoryError):
    """Raised when an invalid product type is specified."""
    def __init__(self, product_type: str):
        self.product_type = product_type
        super().__init__(f"Invalid product type: {product_type}") 