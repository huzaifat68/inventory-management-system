
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

    # Method for adjusting stock
    def adjust_stock(self):
        if self.current_user.role == "Admin":
            try:
                product_id = int(input("Enter product ID to adjust stock: "))
                product = self.products.get(product_id)
                if product:
                    quantity = int(input("Enter quantity to add adjust stock ( '+' to add and '-' to reduce): "))
                    product.stock_update(quantity)
                else:
                    print("Product not found")
            except ValueError:
                print("Error: Please enter a valid Product ID and Quantity.")
        else:
            print("Access denied. Users with the admin role can add product.")

    # Method for sale
    def sale(self):
        try:
            product_id = int(input("Enter Product ID to sell: "))
            product = self.products.get(product_id)
            if product:
                quantity = int(input("Enter quantity to sell: "))
                if quantity > 0 and quantity >= product.stock:
                    product.stock_update(-quantity)
                    print(f"Sale completed, {quantity} units of the {product.name} sold")
                else:
                    print(f"Error: Invalid Quanity, Current stock {product.stock}")
            else:
                print("Error: Product not found in record")
        except ValueError:
            print("Error: Please enter a valid Product ID and quantity.")


if __name__ == "__main__":
    ims = InventoryManagementSystem()
    
    ims.add_user("admin", "admin123", "Admin")
    ims.add_user("user", "user123", "User")

    print("Welcome to Console base Inventory Management System (IMS)")
    while True:
        if ims.login():
            while True:
                if ims.current_user.role == "Admin":
                    print("1: Add Product\n2: Edit Product\n3: Delete Product\n4: View Inventory\n5: Adjust Stock\n6: Record a Sale\n7: Logout")
                else:
                    print("1: View Inventory\n2: Recod a Sale\n3: Logout")

                choice = input("Choose an option: ")

                if ims.current_user.role == "Admin":
                    if choice == "1":
                      ims.add_product()
                    if choice == "2":
                        ims.edit_product()
                    if choice == "3":
                        ims.delete_product()
                    if choice == "4":
                        ims.view_inventory()
                    if choice == "5":
                        ims.adjust_stock()
                    if choice == "6":
                        ims.sale()
                    if choice == "7":
                        print("Loggin out...")
                        ims.current_user.role = None
                        break
                    else:
                        print("Error: Invalid Choice. Try Again")
                else:
                    if choice == "1":
                        ims.view_inventory()
                    if choice == "2":
                        ims.sale()
                    if choice == "3":
                        print("Loggin out...")
                        ims.current_user.role = None
                        break
                    else:
                        print("Error: Invalid Choice. Try Again")
        else:
            print("Login failed. Try again")