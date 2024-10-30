
#User class for managing roles based access
class User:
    def __init__(self,username,password,role):
        self.username = username
        self.password = password
        self.role = role 


# Product class for managing and creating products
class Product:
    def __init__(self,product_id,name,catagory,price,stock):
        self.product_id = product_id
        self.name = name
        self.catagory = catagory
        self.price = price
        self.stock = stock
    
    # Method for updating stock
    def stock_update(self,quantity):
        if self.stock + quantity < 0:
            print(f"Error: Not enough stock, current stock is {self.stock}.")
        else:
            self.stock += quantity
            print(f"Stock updated for {self.name}, New stock is {self.stock}.")

    # Method for viewing product information
    def view_product(self):
        return (f"ID: {self.product_id}, Name: {self.name}, Catagory: {self.catagory},"
        f"Price: {self.price}, Stock: {self.stock}.")
            



class InventoryManagementSystem:
   # Initialize the system , storing user, product and current user  
    def __init__(self):
        self.users = []
        self.products = {}
        self.current_user = None

    # Method for adding user
    def add_user(self,username,password,role):
        user = User(username,password,role)
        self.users.append(user)

    # Method for login
    def login(self):
        username = input("Enter username:")
        password = input("Enter password:")
        for user in self.users:
            if user.username == username and user.password == password:
                print(f"Welcome {user.username}! You are logged in as {user.role}.")
                self.current_user = user
                return True
            else:
                print("You have enterd wrong username or password.")
                return False
        
    # Method for adding product
    def add_product(self):
        if self.current_user.role == "Admin":
            product_id = int(input("Enter Product ID: "))
            name = str(input("Enter Product Name: "))
            catagory = str(input("Enter Product Category: "))
            price = float(input("Enter Product Price: "))
            stock_quantity = int(input("Enter Product Stock: "))
            product = Product(product_id,name, catagory,price,stock_quantity)
            self.products[product_id] = product
            print(f"{name} product added in inventory.")
        else:
            print("Access denied. Users with the admin role can add product.")

    # Method to edit the product
    def edit_product(self):
        if self.current_user.role == "Admin":
            prodcut_id = int(input("Enter product ID: "))
            product = self.products.get(prodcut_id)
            if product:
                product.name = input("Enter new product Name: ")
                product.catagory = input("Enter new product Catagory: ")
                product.price = input("Enter new product Price: ")
                product.stock_quantity = input("Enter new product Stock: ")
            else:
                print("Product not found.")
        else:
            print("Access denied. Users with the admin role can add product.")

    # Method for deleting product
    def delete_product(self):
        if self.current_user.role == "Admin":
            product_id = int(input("Enter product ID to delete the product: "))
            if product_id in self.products:
                del self.products[product_id]
                print(f"Product with the ID {product_id} has been deleted.")
        else:
            print("Access denied. Users with the admin role can add product.")
 
    # Method for viewing inventory
    def view_inventory(self):
        print("Current Inventory:")
        for product in self.products.values():
            print(product.view_product())
