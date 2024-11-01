
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

        self.default_user()


    # Adding default user
    def default_user(self):
        admin_user = User("admin","admin123","Admin")
        user_1 = User("user1","user123","User")
        self.users.append(admin_user)
        self.users.append(user_1)

    # Method for login
    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user.username == username and user.password == password:
                print(f"Welcome {user.username}! You are logged in as {user.role}.")
                self.current_user = user
                return True
            
        print("You have enterd wrong username or password.")
        return False


    # Method for adding user
    def add_user(self):
        if self.current_user and self.current_user.role== "Admin":
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            role = input("Enter new role (Admin/User): ").capitalize()
            user = User(username,password,role)
            self.users.append(user)
            print(f"User {username} with the role {role} added")

        else:
            print("Access denied. Users with the admin role can add users.")


        
    # Method for adding product
    def add_product(self):
        if self.current_user.role == "Admin":
            try:
                product_id = int(input("\nEnter Product ID: "))

                if product_id in self.products:
                    print("\nError: Product ID already exist. Please enter a unique ID.")
                    return


                
                name = str(input("Enter Product Name: "))
                catagory = str(input("Enter Product Category: "))
                price = float(input("Enter Product Price: "))
                stock = int(input("Enter Product Stock: "))
                
                product = Product(product_id,name, catagory,price,stock)
                self.products[product_id] = product
                print(f"{name} product added in inventory.")
            except ValueError:
                print("\nError: Invalid input, Please enter valid numbers for Product ID, Price and Stock")
        else:
            print("\nAccess denied. Users with the admin role can add product.")

    # Method to edit the product
    def edit_product(self):
        if self.current_user.role == "Admin":
            prodcut_id = int(input("Enter product ID: "))
            product = self.products.get(prodcut_id)
            if product:
                product.name = input("Enter new product Name: ")
                product.catagory = input("Enter new product Catagory: ")
                product.price = input("Enter new product Price: ")
                product.stock = input("Enter new product Stock: ")
            else:
                print("Product not found.")
        else:
            print("Access denied. Users with the admin role can Edit product.")

    # Method for deleting product
    def delete_product(self):
        if self.current_user.role == "Admin":
            product_id = int(input("Enter product ID to delete the product: "))
            if product_id in self.products:
                del self.products[product_id]
                print(f"Product with the ID {product_id} has been deleted.")
            else:
                print("\nError: Product not found.")
        else:
            print("Access denied. Users with the admin role can delete product.")
 
    # Method for viewing inventory
    def view_inventory(self):
        print("Current Inventory:")
        for product in self.products.values():
            print(product.view_product())
            print("-" * 50)


    # Method for searching product
    def search_product(self):
        search = input("Enter Product name or Category to search: ").lower()
        product_found = [product.view_product() for product in self.products.values()
                        if search in product.name.lower() or search in product.catagory.lower()]
        if product_found:
            print("Search Result:")
            for product_info in product_found:
                print(product_info)
                print("-" * 50)

        else:
            print("Product not found.")

    # Method for checking stock level
    def stock_check(self):
        try:
            threshold = int(input("Enter threshold stock: "))
            low_stock = [product.view_product() for product in self.products.values() if product.stock <= threshold]
            if low_stock:
                print("Products with low stock:")
                for product_info in low_stock:
                    print(product_info)
                    print("-" * 50)

            else:
                print("All product have more stock than threshold.")
        except ValueError:
            print("Error: Enter a valid quantity for threshold.")

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
            print("Access denied. Users with the admin role can adjust product.")

    # Method for sale
    def sale(self):
        try:
            product_id = int(input("Enter Product ID to sell: "))
            product = self.products.get(product_id)
            if product:
                quantity = int(input("Enter quantity to sell: "))
                if quantity > 0 and quantity <= product.stock:
                    product.stock_update(-quantity)
                    print(f"Sale completed, {quantity} units of the {product.name} sold")
                else:
                    print(f"Error: Invalid Quanity, Current stock {product.stock}")
            else:
                print("Error: Product not found in record")
        except ValueError:
            print("Error: Please enter a valid Product ID and quantity.")


    # Method for checking Users
    def check_users(self):
        if self.current_user.role == "Admin":
            users = self.users

            for user in users:
                print(f"Username: {user.username}, Password: {user.password}, Role: {user.role}")
                print("-" * 50)

        else:
            print("Access denied. Users with the admin role can adjust product.")           



if __name__ == "__main__":
    ims = InventoryManagementSystem()
    
    
    print("Welcome to Console base Inventory Management System (IMS)")
    while True:
        if ims.login():
            while True:
                if ims.current_user.role == "Admin":
                    print("\n1: Add User\n2: Add Product\n3: Edit Product\n4: Delete Product\n5: View Inventory\n6: Adjust Stock\n7: Record a Sale\
                        \n8: Search Product\n9: Check Stock\n10: Check Users\n11: Logout")
                else:
                    print("\n1: View Inventory\n2: Recod a Sale\n3: Search Product\n4: Check Stock\n5: Logout")

                choice = input("Choose an option: ")

                if ims.current_user.role == "Admin":
                    if choice == "1":
                        ims.add_user()
                    elif choice == "2":
                      ims.add_product()
                    elif choice == "3":
                        ims.edit_product()
                    elif choice == "4":
                        ims.delete_product()
                    elif choice == "5":
                        ims.view_inventory()
                    elif choice == "6":
                        ims.adjust_stock()
                    elif choice == "7":
                        ims.sale()
                    elif choice == "8":
                        ims.search_product()
                    elif choice == "9":
                        ims.stock_check()
                    elif choice == "10":
                        ims.check_users()
                    elif choice == "11":
                        print("Loggin out...")
                        ims.current_user = None
                        break
                    else:
                        print("Error: Invalid Choice. Try Again")
               
                else:
                    if choice == "1":
                        ims.view_inventory()
                    elif choice == "2":
                        ims.sale()
                    elif choice == "3":
                        ims.search_product()
                    elif choice == "4":
                        ims.stock_check()
                    elif choice == "5":
                        print("Loggin out...")
                        ims.current_user = None
                        break
                    else:
                        print("Error: Invalid Choice. Try Again")
        else:
            print("Login failed. Try again")