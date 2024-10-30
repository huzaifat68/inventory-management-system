
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
            print(f"Error: Not enough stock, current stock is {self.stock}")
        else:
            self.stock += quantity
            print(f"Stock updated for {self.name}, New stock is {self.stock}")

    # Method for viewing product information
    def view_product(self):
        return (f"ID: {self.product_id}, Name: {self.name}, Catagory: {self.catagory},"
        f"Price: {self.price}, Stock: {self.stock}")
            



class InventoryManagementSystem:
   # Initialize the system , storing user, product and current user  
    def __init__(self):
        self.users = []
        self.product = {}
        self.current_user = None

    # Method for adding user
    def add_user(self,username,password,role):
        user = User(username,password,role)
        self.users.append(user)

    # Method for login
    def login(self):
        username = input("Enter username:")
        password = input("Enter password:")


