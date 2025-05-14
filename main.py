import os
from typing import Optional, Dict, Any
from datetime import datetime
from models.inventory import Inventory
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from exceptions.custom_exceptions import (
    InventoryError,
    InsufficientStockError,
    DuplicateProductError,
    ProductNotFoundError,
    InvalidProductDataError,
    InvalidProductTypeError
)

class InventoryCLI:
    """Command-line interface for the inventory management system."""
    
    def __init__(self):
        """Initialize the CLI with an empty inventory."""
        self.inventory = Inventory()
        self.running = True
    
    def clear_screen(self) -> None:
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self) -> None:
        """Print the application header."""
        print("=" * 50)
        print("Inventory Management System".center(50))
        print("=" * 50)
        print()
    
    def print_menu(self) -> None:
        """Print the main menu options."""
        print("\nMain Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Search Products")
        print("4. List All Products")
        print("5. Sell Product")
        print("6. Restock Product")
        print("7. Remove Expired Products")
        print("8. Save Inventory")
        print("9. Load Inventory")
        print("10. Show Total Inventory Value")
        print("0. Exit")
        print()
    
    def get_product_type(self) -> str:
        """Get the product type from user input."""
        while True:
            print("\nSelect product type:")
            print("1. Electronics")
            print("2. Grocery")
            print("3. Clothing")
            print("0. Back to main menu")
            
            choice = input("\nEnter your choice (0-3): ").strip()
            
            if choice == "0":
                return ""
            elif choice == "1":
                return "Electronics"
            elif choice == "2":
                return "Grocery"
            elif choice == "3":
                return "Clothing"
            else:
                print("Invalid choice. Please try again.")
    
    def get_product_data(self, product_type: str) -> Optional[Dict[str, Any]]:
        """Get product data from user input."""
        try:
            print("\nEnter product details:")
            product_id = input("Product ID: ").strip()
            name = input("Name: ").strip()
            price = float(input("Price: ").strip())
            quantity = int(input("Quantity in stock: ").strip())
            
            if product_type == "Electronics":
                warranty = int(input("Warranty (years): ").strip())
                brand = input("Brand: ").strip()
                return {
                    'product_id': product_id,
                    'name': name,
                    'price': price,
                    'quantity_in_stock': quantity,
                    'warranty_years': warranty,
                    'brand': brand
                }
            elif product_type == "Grocery":
                expiry = input("Expiry date (YYYY-MM-DD): ").strip()
                return {
                    'product_id': product_id,
                    'name': name,
                    'price': price,
                    'quantity_in_stock': quantity,
                    'expiry_date': expiry
                }
            elif product_type == "Clothing":
                size = input("Size: ").strip()
                material = input("Material: ").strip()
                return {
                    'product_id': product_id,
                    'name': name,
                    'price': price,
                    'quantity_in_stock': quantity,
                    'size': size,
                    'material': material
                }
        except ValueError as e:
            print(f"Error: Invalid input - {str(e)}")
            return None
    
    def add_product(self) -> None:
        """Add a new product to the inventory."""
        product_type = self.get_product_type()
        if not product_type:
            return
        
        product_data = self.get_product_data(product_type)
        if not product_data:
            return
        
        try:
            if product_type == "Electronics":
                product = Electronics(**product_data)
            elif product_type == "Grocery":
                product = Grocery(**product_data)
            else:  # Clothing
                product = Clothing(**product_data)
            
            self.inventory.add_product(product)
            print("\nProduct added successfully!")
        except InventoryError as e:
            print(f"\nError: {str(e)}")
    
    def remove_product(self) -> None:
        """Remove a product from the inventory."""
        product_id = input("\nEnter product ID to remove: ").strip()
        try:
            self.inventory.remove_product(product_id)
            print("\nProduct removed successfully!")
        except ProductNotFoundError as e:
            print(f"\nError: {str(e)}")
    
    def search_products(self) -> None:
        """Search for products in the inventory."""
        print("\nSearch options:")
        print("1. Search by name")
        print("2. Search by type")
        print("0. Back to main menu")
        
        choice = input("\nEnter your choice (0-2): ").strip()
        
        if choice == "0":
            return
        elif choice == "1":
            name = input("\nEnter product name to search: ").strip()
            products = self.inventory.search_by_name(name)
        elif choice == "2":
            product_type = self.get_product_type()
            if not product_type:
                return
            try:
                products = self.inventory.search_by_type(product_type)
            except InvalidProductTypeError as e:
                print(f"\nError: {str(e)}")
                return
        else:
            print("Invalid choice.")
            return
        
        if not products:
            print("\nNo products found.")
        else:
            print(f"\nFound {len(products)} products:")
            for product in products:
                print("\n" + "=" * 30)
                print(product)
    
    def list_products(self) -> None:
        """List all products in the inventory."""
        products = self.inventory.list_all_products()
        if not products:
            print("\nInventory is empty.")
        else:
            print(f"\nInventory ({len(products)} products):")
            for product in products:
                print("\n" + "=" * 30)
                print(product)
    
    def sell_product(self) -> None:
        """Sell a quantity of a product."""
        product_id = input("\nEnter product ID: ").strip()
        try:
            quantity = int(input("Enter quantity to sell: ").strip())
            total = self.inventory.sell_product(product_id, quantity)
            print(f"\nSale successful! Total: ${total:.2f}")
        except (ValueError, ProductNotFoundError, InsufficientStockError) as e:
            print(f"\nError: {str(e)}")
    
    def restock_product(self) -> None:
        """Restock a product."""
        product_id = input("\nEnter product ID: ").strip()
        try:
            quantity = int(input("Enter quantity to add: ").strip())
            self.inventory.restock_product(product_id, quantity)
            print("\nProduct restocked successfully!")
        except (ValueError, ProductNotFoundError) as e:
            print(f"\nError: {str(e)}")
    
    def remove_expired(self) -> None:
        """Remove expired grocery products."""
        expired_ids = self.inventory.remove_expired_products()
        if not expired_ids:
            print("\nNo expired products found.")
        else:
            print(f"\nRemoved {len(expired_ids)} expired products:")
            for product_id in expired_ids:
                print(f"- {product_id}")
    
    def save_inventory(self) -> None:
        """Save the inventory to a file."""
        filename = input("\nEnter filename to save (default: inventory.json): ").strip()
        if not filename:
            filename = "inventory.json"
        
        try:
            self.inventory.save_to_file(filename)
            print("\nInventory saved successfully!")
        except Exception as e:
            print(f"\nError saving inventory: {str(e)}")
    
    def load_inventory(self) -> None:
        """Load the inventory from a file."""
        filename = input("\nEnter filename to load (default: inventory.json): ").strip()
        if not filename:
            filename = "inventory.json"
        
        try:
            self.inventory = Inventory.load_from_file(filename)
            print("\nInventory loaded successfully!")
        except InvalidProductDataError as e:
            print(f"\nError loading inventory: {str(e)}")
    
    def show_total_value(self) -> None:
        """Show the total value of the inventory."""
        total = self.inventory.total_inventory_value()
        print(f"\nTotal inventory value: ${total:.2f}")
    
    def run(self) -> None:
        """Run the main CLI loop."""
        while self.running:
            self.clear_screen()
            self.print_header()
            self.print_menu()
            
            choice = input("Enter your choice (0-10): ").strip()
            
            if choice == "0":
                self.running = False
            elif choice == "1":
                self.add_product()
            elif choice == "2":
                self.remove_product()
            elif choice == "3":
                self.search_products()
            elif choice == "4":
                self.list_products()
            elif choice == "5":
                self.sell_product()
            elif choice == "6":
                self.restock_product()
            elif choice == "7":
                self.remove_expired()
            elif choice == "8":
                self.save_inventory()
            elif choice == "9":
                self.load_inventory()
            elif choice == "10":
                self.show_total_value()
            else:
                print("\nInvalid choice. Please try again.")
            
            if self.running:
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    cli = InventoryCLI()
    cli.run() 