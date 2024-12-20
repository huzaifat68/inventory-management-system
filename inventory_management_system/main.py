"""
Console Based Inventory Management System

Default Users:
username = admin, user1
password = admin123, user123
"""

import csv,datetime

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
        try:
            if self.stock + quantity < 0:
                print(f"Error: Not enough stock, current stock is {self.stock}.")
            else:
                self.stock += quantity
                print(f"Stock updated for {self.name}, New stock is {self.stock}.")
        except Exception as e:
            print(f"Unexpected error while updating stock: {e}")


    # Method for viewing product information
    def view_product(self):
        try:
            return (f"ID: {self.product_id}, Name: {self.name}, Catagory: {self.catagory},"
            f"Price: {self.price}, Stock: {self.stock}.")
        except Exception as e:
            print(f"Error while viewing product: {e}")
            return None    


class InventoryManagementSystem:

   # Initialize the system , storing user, product and current user  
    def __init__(self):
        self.users = []
        self.products = {}
        self.sales = []
        self.current_user = None
        self.default_user()


    # Adding default user
    def default_user(self):
        try:
            admin_user = User("admin","admin123","Admin")
            user_1 = User("user1","user123","User")
            self.users.append(admin_user)
            self.users.append(user_1)
        except Exception as e:
            print(f"Error while creating default users: {e}")


    # Method for login
    def login(self):
        try:
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            for user in self.users:
                if user.username == username and user.password == password:
                    print(f"\nWelcome {user.username}! You are logged in as {user.role}.")
                    self.current_user = user
                    return True
                
            print("You have enterd wrong username or password.")
            return False
        except Exception as e:
            print(f"Unexpected error during login: {e}")
            return False


    # Method for adding user
    def add_user(self):
        if self.current_user and self.current_user.role== "Admin":
            try:
                username = input("\nEnter new username: ")
                password = input("Enter new password: ")
                role = input("Enter new role (Admin/User): ").capitalize()
                user = User(username,password,role)
                self.users.append(user)
                print(f"User {username} with the role {role} added")
            except ValueError:
                print("Error: Invalid input for user details.")
            except Exception as e:
                print(f"Unexpected error while adding user: {e}")
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
                print("\nError: Invalid input. Please enter valid numbers for Product ID, Price, and Stock.")
            except Exception as e:
                print(f"Unexpected error while adding product: {e}")
        else:
            print("\nAccess denied. Users with the admin role can add product.")


    # Method to edit the product
    def edit_product(self):
        if self.current_user.role == "Admin":
            try:
                product_id = int(input("\nEnter product ID: "))
                product = self.products.get(product_id)
                if product:
                    product.name = input("Enter new product Name: ")
                    product.catagory = input("Enter new product Catagory: ")
                    product.price = input("Enter new product Price: ")
                    product.stock = input("Enter new product Stock: ")
                else:
                    print("Product not found.")
            except ValueError:
                print("Error: Invalid input for product details.")
            except Exception as e:
                print(f"Unexpected error while editing product: {e}")
        else:
            print("Access denied. Users with the admin role can Edit product.")


    # Method for deleting product
    def delete_product(self):
        
        if self.current_user.role == "Admin":
            try:
                product_id = int(input("Enter product ID to delete the product: "))
                if product_id in self.products:
                    del self.products[product_id]
                    print(f"\nProduct with the ID {product_id} has been deleted.")
                else:
                    print("\nError: Product not found.")
            except ValueError:
                print("Error: Invalid Product ID.")
            except Exception as e:
                print(f"Unexpected error while deleting product: {e}")
        else:
                print("Access denied. Users with the admin role can delete product.")
        


    # Method for viewing inventory
    def view_inventory(self):
        try:
            print("Current Inventory:")
            for product in self.products.values():
                print(product.view_product())
                print("-" * 60)
        except Exception as e:
            print(f"Unexpected error while viewing inventory: {e}")


    # Method for searching product
    def search_product(self):
        try:
            search = input("\nEnter Product name or Category to search: ").lower()
            product_found = [product.view_product() for product in self.products.values()
                            if search in product.name.lower() or search in product.catagory.lower()]
            if product_found:
                print("Search Result:")
                for product_info in product_found:
                    print(product_info)
                    print("-" * 50)
            else:
                print("Product not found.")
        except Exception as e:
            print(f"Unexpected error while searching for product: {e}")


    # Method for checking stock level
    def stock_check(self):
        try:
            threshold = int(input("\nEnter threshold stock: "))
            low_stock = [product.view_product() for product in self.products.values() if product.stock <= threshold]
            if low_stock:
                print("\nProducts with low stock:")
                for product_info in low_stock:
                    print(product_info)
                    print("-" * 50)
            else:
                print("All product have more stock than threshold.")
        except ValueError:
            print("Error: Invalid input for threshold.")
        except Exception as e:
            print(f"Unexpected error during stock check: {e}")


    # Method for adjusting stock
    def adjust_stock(self):
            if self.current_user.role == "Admin":
                try:
                    product_id = int(input("\nEnter product ID to adjust stock: "))
                    product = self.products.get(product_id)
                    if product:
                        quantity = int(input("Enter quantity to add adjust stock ( '+' to add and '-' to reduce): "))
                        product.stock_update(quantity)
                    else:
                        print("Product not found.")
                except ValueError:
                    print("Error: Please enter a valid Product ID and Quantity.")
                except Exception as e:
                    print(f"Unexpected error during stock check: {e}")
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
                    sale_amount = quantity * product.price
                    product.stock_update(-quantity)
                    
                    # Record the sale
                    sale_record = {
                        "Product ID": product_id,
                        "Product Name": product.name,
                        "Quantity Sold": quantity,
                        "Sale Amount": sale_amount,
                        "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    self.sales.append(sale_record)

                    print(f"\nSale completed: {quantity} units of {product.name} sold. Remaining stock: {product.stock}")
                else:
                    print(f"Error: Invalid Quantity. Current stock: {product.stock}")
            else:
                print("Error: Product not found in record")
        except ValueError:
            print("Error: Invalid input for Product ID or quantity.")
        except Exception as e:
            print(f"Unexpected error while processing sale: {e}")


    # Method to export sales to csv
    def export_sales_to_csv(self):
        if self.current_user.role == "Admin":
            try:
                filename = input("Enter the filename to export sales (default: sales.csv): ") or "sales.csv"
                
                # Check if there are sales to export
                if not self.sales:
                    print("No sales data to export.")
                    return

                # Write sales data to a CSV file
                with open(filename, mode="w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=self.sales[0].keys())
                    writer.writeheader()
                    writer.writerows(self.sales)
                    
                print(f"Sales data successfully exported to '{filename}'.")
            except PermissionError:
                print(f"Error: Permission denied. Please close the file '{filename}' if it is open and try again.")
            except Exception as e:
                print(f"Unexpected error while exporting sales: {e}")
        else:
            print("Access denied. Only admins can export sales data.")


    # Method for checking Users
    def check_users(self):
            if self.current_user.role == "Admin":
                try:
                    users = self.users

                    for user in users:
                        print(f"Username: {user.username}, Password: {user.password}, Role: {user.role}")
                        print("-" * 50)
                except Exception as e:
                    print(f"Unexpected error while checking users: {e}")
            else:
                print("Access denied. Users with the admin role can check users.")  



    # Method for deleting user
    def delete_user(self):
        
        if self.current_user.role == "Admin":
            try:
                username = input("Enter username to delete user: ")
                password = input("Enter password to delete user: ")

                if username == self.current_user.username:
                    print("Error: You cannot delete the account you are currently logged in with.")
                    return

                user_to_del = None
                for user in self.users:
                            
                    if user.username == username and user.password == password:
                        user_to_del = user
                        break

                if user_to_del:
                    self.users.remove(user_to_del)
                    print(f"\nUser '{username}' has been deleted successfully.")
                            
                else:
                    print("Error: User not found.")  
            except Exception as e:
                print(f"Unexpected error while deleting user {e}")          
        else:
            print("Access denied. Users with the admin role can delete users.")
        

    # Method for changing the password (Admin only)
    def change_password(self):
        if self.current_user.role == "Admin":
            try:
                username = input("\nEnter the username of the account to change the password: ")
                user_to_update = None

                # Find the user
                for user in self.users:
                    if user.username == username:
                        user_to_update = user
                        break

                if user_to_update:
                    new_password = input("Enter the new password: ")
                    confirm_password = input("Confirm the new password: ")
                    
                    if new_password == confirm_password:
                        user_to_update.password = new_password
                        print(f"Password for user '{username}' has been updated successfully!")
                    else:
                        print("Error: New password and confirm password do not match.")
                else:
                    print("Error: User not found.")
            except Exception as e:
                print("An unexpected error occurred while changing the password.")
                print(f"Debug info: {e}")
        else:
            print("Access denied. Only admins can change passwords.")
   

    # Method to export inventory to CSV
    def export_inventory_to_csv(self):
        if self.current_user.role == "Admin":
            try:
                filename = input("Enter the filename to export inventory (default: inventory.csv): ") or "inventory.csv"
                data = []

                # Prepare the data for CSV export
                for product in self.products.values():
                    data.append({
                        "Product ID": product.product_id,
                        "Name": product.name,
                        "Category": product.catagory,
                        "Price": product.price,
                        "Stock": product.stock
                    })

                # Write data to CSV
                if not data:
                    print("No inventory data to export.")
                else:
                    with open(filename, mode="w", newline="") as file:
                        writer = csv.DictWriter(file, fieldnames=data[0].keys())
                        writer.writeheader()
                        writer.writerows(data)
                    print(f"Inventory exported successfully to '{filename}'.")
            except PermissionError:
                print(f"Error: Permission denied. Please close the file '{filename}' if it is open and try again.")
            except Exception as e:
                print(f"Unexpected error while exporting inventory: {e}")
        else:
            print("Access denied. Only admins can export inventory.")



if __name__ == "__main__":
    try:
        ims = InventoryManagementSystem()
        print("Welcome to Console-based Inventory Management System (IMS)")
        
        while True:
            try:
                if ims.login():
                    while True:
                        if ims.current_user.role == "Admin":
                            print("\n1: Add User\n2: Add Product\n3: Edit Product\n4: Delete Product\n5: View Inventory\n6: Adjust Stock\n7: Record a Sale\
                                \n8: Search Product\n9: Check Stock\n10: Check Users\n11: Delete User\n12: Change Password\n13: Export Inventory\n14: Export Sales\
                                  \n15: Logout\n16: Exit program")
                        else:
                            print("\n1: View Inventory\n2: Record a Sale\n3: Search Product\n4: Check Stock\n5: Logout\n6: Exit program")

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
                                ims.delete_user()
                            elif choice == "12":
                                ims.change_password()
                            elif choice == "13":
                                ims.export_inventory_to_csv()
                            elif choice == "14":
                                ims.export_sales_to_csv()
                            elif choice == "15":
                                print("Logging out...")
                                ims.current_user = None
                                break
                            elif choice == "16":
                                exit()
                                
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
                                print("Logging out...")
                                ims.current_user = None
                                break
                            elif choice == "6":
                                exit()
                            else:
                                print("Error: Invalid Choice. Try Again")
            
            except AttributeError as e:
                print("Error: It seems there was an issue with accessing user attributes. Please check the user settings or contact support.")
                print(f"Debug info: {e}")

            except Exception as e:
                print("An unexpected error occurred during the login session.")
                print(f"Debug info: {e}")

    except KeyboardInterrupt:
        print("\nProgram terminated by the user. Exiting...")

    except Exception as e:
        print("An unexpected error occurred during program initialization.")
        print(f"Debug info: {e}")