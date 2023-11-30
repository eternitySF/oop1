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

    def __str__(self):
        return f"{self.name} - {self.price} грн"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False


class ElectronicProduct(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def get_description(self):
        return f"{super().get_description()} by {self.brand}"

    def __str__(self):
        return f"{super().__str__()} by {self.brand}"

    def __repr__(self):
        return f"ElectronicProduct('{self.name}', {self.price}, '{self.brand}')"


class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_description(self):
        return f"{super().get_description()} (Size {self.size})"

    def __str__(self):
        return f"{super().__str__()} (Size {self.size})"

    def __repr__(self):
        return f"ClothingProduct('{self.name}', {self.price}, '{self.size}')"


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

print(product1)
print(Product.count)
print(Product.is_discounted(800))

print(phone)
print(shirt)

cart = ShoppingCart()
cart.add_product(phone)
cart.add_product(shirt)

cart.display_cart()

print(isinstance(phone, Product))
print(isinstance(shirt, ElectronicProduct))

print(issubclass(ElectronicProduct, Product))
print(issubclass(ClothingProduct, ElectronicProduct))

product3 = Product("Телефон", 2000)
print(product1 == product3) 
