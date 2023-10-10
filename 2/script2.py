#Створення списків
numbers = []
strings = []
names = ["Денис", "Зиновій", "Кирило"]
#добавлення цифр і слів у списки
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
#присвоєння змінній другого імені
second_name = names[1]
#виводяться наповнені списки з цифрами і словами, вивелось друге ім'я в списку
print(numbers)
print(strings)
print("Друге ім'я у списку -  %s" % second_name)