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