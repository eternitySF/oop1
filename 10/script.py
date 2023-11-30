class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        """Getter для отримання довжини."""
        return self._length

    @property
    def width(self):
        """Getter для отримання ширини."""
        return self._width

    @length.setter
    def length(self, value):
        """Setter для встановлення довжини."""
        if value < 0:
            raise ValueError("Довжина не може бути від'ємною")
        self._length = value

    @width.setter
    def width(self, value):
        """Setter для встановлення ширини."""
        if value < 0:
            raise ValueError("Ширина не може бути від'ємною")
        self._width = value

    @property
    def area(self):
        """Метод, який використовується як властивість для отримання площі прямокутника."""
        return self._length * self._width

    @property
    def perimeter(self):
        """Метод, який використовується як властивість для отримання периметру прямокутника."""
        return 2 * (self._length + self._width)

    @length.deleter
    def length(self):
        """Deleter для видалення довжини."""
        print("Видаляємо довжину")
        del self._length

    @width.deleter
    def width(self):
        """Deleter для видалення ширини."""
        print("Видаляємо ширину")
        del self._width


rectangle = Rectangle(5, 8)
print(f"Довжина: {rectangle.length}")
print(f"Ширина: {rectangle.width}")
print(f"Площа: {rectangle.area}")
print(f"Периметр: {rectangle.perimeter}")

rectangle.length = 10  
rectangle.width = 6    
print(f"Нова довжина: {rectangle.length}")
print(f"Нова ширина: {rectangle.width}")
print(f"Нова площа: {rectangle.area}")
print(f"Новий периметр: {rectangle.perimeter}")

del rectangle.length    