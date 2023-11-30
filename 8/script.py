class Product:
    count = 0

    def __init__(self, name, price):
        self.name, self.price = name, price
        self.description = f"{self.name} - {self.price} грн"
        Product.count += 1

    def get_description(self):
        return self.description

    @classmethod
    def from_string(cls, string):
        name, price = map(str.strip, string.split("-"))
        return cls(name, int(price))

    @staticmethod
    def is_discounted(price):
        return price < 1000


class ElectronicProduct(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def get_description(self):
        return f"{super().get_description()} by {self.brand}"


class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_description(self):
        return f"{super().get_description()} (Size {self.size})"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_cart(self):
        for product in self.products:
            print(product.get_description())


product1 = Product("Телефон", 2000)
product2 = Product.from_string("Ноутбук - 5000")
phone = ElectronicProduct("Смартфон", 3000, "Samsung")
shirt = ClothingProduct("Футболка", 500, "M")

print(product1.get_description())
print(Product.count)
print(Product.is_discounted(800))

print(phone.get_description())
print(shirt.get_description())

cart = ShoppingCart()
cart.add_product(phone)
cart.add_product(shirt)

cart.display_cart()

print(isinstance(phone, Product)) 
print(isinstance(shirt, ElectronicProduct)) 

print(issubclass(ElectronicProduct, Product)) 
print(issubclass(ClothingProduct, ElectronicProduct))  
