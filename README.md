# Inventory Management System

A robust Python-based Inventory Management System that demonstrates advanced Object-Oriented Programming concepts.

## Features

- Abstract base class for products with proper encapsulation
- Multiple product types (Electronics, Grocery, Clothing)
- Comprehensive inventory management
- Data persistence using JSON
- Custom exception handling
- Interactive CLI interface

## Project Structure

```
inventory_management/
├── models/
│   ├── __init__.py
│   ├── product.py
│   ├── electronics.py
│   ├── grocery.py
│   ├── clothing.py
│   └── inventory.py
├── exceptions/
│   ├── __init__.py
│   └── custom_exceptions.py
├── utils/
│   ├── __init__.py
│   └── json_handler.py
├── main.py
└── requirements.txt
```

## Installation

1. Clone the repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main program:
```bash
python main.py
```

## Features

- Add, remove, and search products
- Manage different product types (Electronics, Grocery, Clothing)
- Track inventory levels and sales
- Save and load inventory data
- Handle expired products (for groceries)
- Calculate total inventory value

## Requirements

- Python 3.8+
- See requirements.txt for dependencies

