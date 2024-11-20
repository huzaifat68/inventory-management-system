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
   python inventory_management.py
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

This project is open-source and can be used and modified freely. No warranty is provided, and usage is at your own risk.

## Conclusion

This simple and functional Inventory Management System allows you to efficiently manage product stock and users, with a clear separation of roles for admins and regular users. It is designed for ease of use and can be expanded to accommodate additional features such as reporting or multi-user support.

---
