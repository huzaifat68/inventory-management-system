# Console-Based Inventory Management System

This is a **Python-based console application** designed to manage an inventory system efficiently. It includes features like user management, product management, stock updates, sales recording, and exporting data to CSV files. The application is designed to be role-based, providing **Admin** users with full control and **Standard Users** with limited access.

---

## Features

1. **Role-Based Access Control**:
   - **Admin**:
     - Manage users (add, view, delete, change passwords).
     - Add, edit, delete, and view products.
     - Adjust stock levels.
     - Record and export sales data.
     - Export inventory data to a CSV file.
   - **User**:
     - View products.
     - Record sales.
     - Search for products and check stock levels.

2. **Product Management**:
   - Add new products to the inventory.
   - Edit existing product details.
   - Delete products from the inventory.

3. **Stock Management**:
   - Adjust product stock (add or reduce quantity).
   - View low-stock products based on a threshold.

4. **Sales Management**:
   - Record sales.
   - Automatically adjust stock after a sale.
   - Export sales data to a CSV file.

5. **Data Export**:
   - Export inventory and sales data to CSV files for backup and reporting.

6. **Search Functionality**:
   - Search for products by name or category.

7. **Default Users**:
   - **Admin**: `admin/admin123`
   - **User**: `user1/user123`

---

## Installation

1. Clone or download this repository.
2. Ensure you have Python installed (version 3.13.0 or higher recommended).
3. Run the script using:

   ```bash
   python main.py
   ```

---

## Usage

1. **Login**: 
   - Use the default credentials or create new users via the **Admin** account.
   
2. **Admin Options**:
   - After logging in as Admin, you can:
     1. Add, view, delete, and update users.
     2. Add, edit, delete, and view products.
     3. Adjust stock levels.
     4. Record sales and view sales data.
     5. Export inventory or sales data to CSV files.

3. **User Options**:
   - After logging in as a regular user, you can:
     1. View the inventory.
     2. Record sales.
     3. Search for products by name or category.
     4. Check stock levels.

---

## Classes and Functions Overview

### 1. **User Class**
   Represents a system user with the following attributes:
   - `username`: The user's login name.
   - `password`: The user's password.
   - `role`: Either `Admin` or `User`.

---

### 2. **Product Class**
   Represents a product in the inventory with attributes and methods:
   - **Attributes**:
     - `product_id`: A unique identifier for the product.
     - `name`: The name of the product.
     - `catagory`: The product's category.
     - `price`: The price of the product.
     - `stock`: The current stock level of the product.
   - **Methods**:
     - `stock_update(quantity)`: Adjusts the stock by adding or subtracting a specified quantity.
     - `view_product()`: Returns a formatted string with product details.

---

### 3. **InventoryManagementSystem Class**

#### Key Methods:

##### User Management:
- `default_user()`: Creates default Admin and User accounts.
- `login()`: Handles user authentication.
- `add_user()`: Allows Admin to add a new user.
- `delete_user()`: Allows Admin to remove a user.
- `check_users()`: Displays all users (Admin only).
- `change_password()`: Allows Admin to change a user's password.

##### Product Management:
- `add_product()`: Adds a new product to the inventory (Admin only).
- `edit_product()`: Edits an existing product's details (Admin only).
- `delete_product()`: Deletes a product from the inventory (Admin only).
- `view_inventory()`: Displays the current inventory.
- `search_product()`: Searches for products by name or category.

##### Stock Management:
- `adjust_stock()`: Adjusts the stock of a specific product (Admin only).
- `stock_check()`: Displays products with stock below a specified threshold.

##### Sales Management:
- `sale()`: Records a sale, adjusts stock, and logs the transaction.
- `export_sales_to_csv()`: Exports sales data to a CSV file (Admin only).

##### Data Export:
- `export_inventory_to_csv()`: Exports the current inventory to a CSV file (Admin only).

---

## Default Credentials

| Username | Password | Role  |
|----------|----------|-------|
| admin    | admin123 | Admin |
| user1    | user123  | User  |

---

## Usage Flow

1. **Login**:
   - Enter your username and password.
   - Admins and Users will see different menu options.

2. **Admin Menu**:
   ```
   1: Add User
   2: Add Product
   3: Edit Product
   4: Delete Product
   5: View Inventory
   6: Adjust Stock
   7: Record a Sale
   8: Search Product
   9: Check Stock
   10: Check Users
   11: Delete User
   12: Change Password
   13: Export Inventory
   14: Export Sales
   15: Logout
   ```

3. **User Menu**:
   ```
   1: View Inventory
   2: Record a Sale
   3: Search Product
   4: Check Stock
   5: Logout
   ```

---

## Error Handling

- The program is designed to handle common errors gracefully, such as:
  - Invalid input (e.g., entering text where numbers are expected).
  - Permission errors during file export.
  - Attempts to access Admin-only features as a regular user.

---

## Example Workflow

1. Admin logs in with `admin/admin123`.
2. Admin adds a new product to the inventory.
3. Admin adjusts stock levels or deletes a product.
4. User logs in with `user1/user123`.
5. User views the inventory and records a sale.
6. Admin exports sales and inventory data to CSV for reporting.

---

## Contributing

Feel free to suggest improvements or fork the repository to add new features. Always test your changes thoroughly before making pull requests.

---