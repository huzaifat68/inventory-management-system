# Console-Based Inventory Management System

A robust Python-based inventory management system designed for efficient tracking of products, managing stock levels, handling user roles, and facilitating sales operations. This program supports both **Admin** and **User** roles, offering a menu-driven interface for seamless interaction.

---

## Features

### User Management
- **Admin Role**:  
  - Add, edit, delete users.  
  - Change passwords for any user.  
  - View all registered users.
- **User Role**:  
  - Limited access to view inventory, record sales, and check stock.

### Product Management
- Add new products with unique IDs.
- Edit product details (name, category, price, stock).
- Delete products from the inventory.
- Search products by name or category.
- View all inventory details in a tabular format.

### Inventory Operations
- Monitor stock levels with a threshold check for low stock.  
- Adjust stock quantities (both increment and decrement).  
- View inventory to see product details like ID, name, category, price, and stock.

### Sales Management
- Record sales and automatically update stock levels.
- Prevent sales exceeding available stock.  

### Exception Handling
- Robust error handling for invalid inputs, access violations, and operational errors.  
- Clear prompts and error messages for seamless user experience.

### Access Control
- Secure system with role-based permissions.  
- Default users for quick setup and testing.

---

## Prerequisites

1. Python 3.8+ must be installed on your system.
2. Clone or download this repository to your local machine.
3. Ensure the Python environment is correctly configured to execute the program.

---

## How to Run the Program

1. Open a terminal or command prompt.
2. Navigate to the directory containing the program file.
3. Execute the program using the command:  
   ```bash
   python main.py
4. Log in using the default credentials or a registered user account:
   - **Admin**:  
     - Username: `admin`  
     - Password: `admin123`
   - **User**:  
     - Username: `user1`  
     - Password: `user123`

---

## User Roles

### Admin Role
Admins have full control of the system, including:  
- Adding, editing, and deleting users or products.  
- Managing inventory operations such as stock adjustments and product deletions.  
- Viewing all registered users.  
- Changing user passwords.  

### User Role
Users have limited access to:  
- View inventory.  
- Record product sales.  
- Search for products by name or category.  
- Monitor stock levels.

---

## Default Users

To get started quickly, the following users are pre-configured:  

| **Username** | **Password** | **Role**  |
|--------------|--------------|-----------|
| admin        | admin123     | Admin     |
| user1        | user123      | User      |

---

## Operations

### 1. Adding a User (Admin Only)
Admins can register new users with a unique username, password, and role.

### 2. Managing Products (Admin Only)
Admins can add new products, edit existing ones, delete products, or view inventory.

### 3. Searching Products
Users and Admins can search for products by name or category to get detailed results.

### 4. Recording Sales
Products can be sold by providing the product ID and quantity. The system ensures sufficient stock is available before proceeding.

### 5. Monitoring Stock Levels
Admins and Users can check inventory status. Products with stock levels below a specified threshold are flagged.

---

## Example Menu Options

### Admin Menu
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
13: Logout
```

### User Menu
```
1: View Inventory  
2: Record a Sale  
3: Search Product  
4: Check Stock  
5: Logout
```

---

## Exception Handling

The program includes comprehensive error handling:
- **Invalid Inputs**: Prompts for correct data types when invalid inputs are entered.  
- **Role-Based Access Control**: Prevents unauthorized actions based on user roles.  
- **Operational Errors**: Handles scenarios like duplicate product IDs, insufficient stock, and unregistered users.  

---

## Limitations

- The system does not use a database, meaning all data is stored temporarily and lost upon program exit.
- Features like multi-threading, real-time updates, and persistent storage can be added for scalability.

---

## Future Improvements

- Integration with a database for persistent storage.
- Enhanced reporting tools for sales and inventory trends.
- User interface improvements with graphical elements.

---

## License

This project is open-source and available for modification under the MIT License.

---

## Author

Developed by Muhammad Huzaifa Tahir. Contributions and feedback are welcome!

---
