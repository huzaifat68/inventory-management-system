# Console-Based Inventory Management System (IMS)

This is a console-based Inventory Management System (IMS) built in Python, designed to manage products, users, stock levels, and sales transactions. The system allows users with the `Admin` role to manage users, products, stock, and more. It features an easy-to-use interface with role-based access for both admins and regular users.

## Features

### User Management
- **Admin Role**: 
  - Add, edit, or delete users.
  - Change user passwords.
  - View all users and their roles.
  
- **User Role**:
  - Regular users can only view the inventory and record sales.

### Product Management
- **Admin Role**: 
  - Add, edit, or delete products.
  - View and search products by name or category.
  - Export inventory data to a CSV file.
  
- **Product Details**: 
  - Each product contains the following information: Product ID, Name, Category, Price, and Stock.

### Stock Management
- **Adjust Stock**: Admins can update product stock levels.
- **Sale**: Regular users and admins can sell products, which will update the stock accordingly.
- **Stock Check**: Admins can view products with stock levels below a specified threshold.

### Inventory
- View the entire inventory with detailed product information.

### Export Inventory
- Admin users can export the current inventory to a CSV file.

## Default Users

- **Admin User**: 
  - Username: `admin`
  - Password: `admin123`
  - Role: `Admin`

- **Regular User**: 
  - Username: `user1`
  - Password: `user123`
  - Role: `User`

## How to Run the Program

1. Clone or download the repository.
2. Ensure that Python 3.x is installed on your system.
3. Run the Python file:

   ```bash
   python ims_system.py
   ```

4. Follow the on-screen prompts to log in using the default users or add new users if you're an admin.

## Requirements

- Python 3.x
- No additional libraries required (uses built-in libraries like `csv`).

## Functionality Breakdown

### User Class
- **Attributes**: 
  - `username`: The username of the user.
  - `password`: The password for authentication.
  - `role`: The user's role (`Admin` or `User`).
  
### Product Class
- **Attributes**:
  - `product_id`: Unique identifier for the product.
  - `name`: The name of the product.
  - `catagory`: The category to which the product belongs.
  - `price`: The price of the product.
  - `stock`: The current stock level of the product.

- **Methods**:
  - `stock_update(quantity)`: Updates the stock by the specified quantity (positive for adding, negative for reducing).
  - `view_product()`: Displays the product details.

### InventoryManagementSystem Class
This class acts as the main controller for the entire system, managing users, products, and transactions. Key methods include:
  
- **User Management**:
  - `add_user()`: Adds a new user (Admin only).
  - `delete_user()`: Deletes an existing user (Admin only).
  - `change_password()`: Allows an Admin to change a user's password.
  
- **Product Management**:
  - `add_product()`: Adds a new product (Admin only).
  - `edit_product()`: Edits an existing product (Admin only).
  - `delete_product()`: Deletes a product (Admin only).
  - `view_inventory()`: Displays all products in the inventory.
  - `search_product()`: Searches for products by name or category.
  - `export_inventory_to_csv()`: Exports the inventory to a CSV file (Admin only).
  
- **Stock Management**:
  - `adjust_stock()`: Allows an Admin to update stock levels.
  - `stock_check()`: Displays products with stock below a certain threshold.
  
- **Sales Management**:
  - `sale()`: Records a sale, updating stock levels accordingly.

### Error Handling
The system handles various types of exceptions such as:
- Value errors (invalid input types)
- Attribute errors (issues with user attributes)
- General unexpected errors, with informative messages.

### Role-Based Access
- **Admin**: Full access to manage users, products, and inventory.
- **User**: Limited access to view inventory and record sales.

## Example of Use

1. **Login as Admin**: 
   - Enter `admin` as username and `admin123` as password.
   - Admin has access to all functionality (adding products, managing users, etc.).
   
2. **Login as User**:
   - Enter `user1` as username and `user123` as password.
   - Users can only view the inventory, search for products, and record sales.

3. **Adding a Product**:
   - Admin can add products using the `add_product()` method, entering details like ID, name, category, price, and stock.

4. **Selling a Product**:
   - Users can record sales by selecting the product and entering the quantity sold. The stock will be updated automatically.

## Troubleshooting

### Common Errors:
- **Invalid Credentials**: Ensure that the username and password match the default or registered users.
- **Product ID Already Exists**: Ensure that each product has a unique ID when adding products.
- **Stock Updates**: Make sure the quantity to be adjusted does not exceed the available stock.

## License

This project is open-source and can be used and modified freely. No warranty is provided, and usage is at your own risk.

## Conclusion

This simple and functional Inventory Management System allows you to efficiently manage product stock and users, with a clear separation of roles for admins and regular users. It is designed for ease of use and can be expanded to accommodate additional features such as reporting or multi-user support.

---