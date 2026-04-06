
class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.total_amount = 0.0  

    def calculate_total(self):
        self.total_amount = self.price * self.quantity
        return self.total_amount

    def disp(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Price per unit: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Amount: ${self.total_amount:.2f}")

        p_id = int(input("Enter Product ID: "))
        p_name = input("Enter Product Name: ")
        price = float(input("Enter Price: $"))
        quantity = int(input("Enter Quantity: "))
        product1 = Product(p_id, p_name, price, quantity)
        product1.calculate_total()
        product1.disp()

