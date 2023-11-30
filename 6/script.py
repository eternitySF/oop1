class Product:
    count = 0  
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.description = f"{self.name} - {self.price} грн"
        Product.count += 1

    def get_description(self):
        return self.description

    @classmethod
    def get_count(cls):
        return cls.count


product1 = Product("Телефон", 2000)
product2 = Product("Ноутбук", 5000)

print(product1.get_description())
print(Product.get_count())