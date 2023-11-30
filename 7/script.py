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
    def from_string(cls, string):
        name, price = string.split("-")
        return cls(name.strip(), int(price.strip()))

    @staticmethod
    def is_discounted(price):
        if price < 1000:
            return True
        return False


product1 = Product("Телефон", 2000)
product2 = Product.from_string("Ноутбук - 5000")

print(product1.get_description())
print(Product.count) 
print(Product.is_discounted(800)) 