# Оголошення класу 
class Vehicle:
    name = ""
    kind = "автомобіль"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s це %s %s який коштує $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# Оголошення об'єктів і введення даних
Car1=Vehicle()
Car1.name="Фер"
Car1.color="червоний"
Car1.kind="кабріолет"
Car1.value=60000.00

Car2=Vehicle()
Car2.name="Джамп"
Car2.color="блакитний"
Car2.kind="фургон"
Car2.value=10000.00
# Тест коду
print(Car1.description())
print(Car2.description())