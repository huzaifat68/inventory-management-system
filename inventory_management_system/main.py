

class User:
    def __init__(self,username,password,role):
        self.username = username
        self.password = password
        self.role = role 


class Product:
    def __init__(self,product_id,name,catagory,price,stock):
        self.product_id = product_id
        self.name = name
        self.catagory = catagory
        self.price = price
        self.stock = stock
    
    def stock_update(self,quantity):
        if self.stock + quantity < 0:
            print(f"Error: Not enough stock, current stock is {self.stock}")
        else:
            self.stock += quantity
            print(f"Stock updated for {self.name}, New stock is {self.stock}")

    def view_product(self):
        return (f"ID: {self.product_id}, Name: {self.name}, Catagory: {self.catagory},"
        f"Price: {self.price}, Stock: {self.stock}")
            



class InventoryManagementSystem:
    def __init__(self):
        self.user = []
        self.product = {}
        self.current_user = None