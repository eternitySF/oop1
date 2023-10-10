x = object()
y = object()
#створення списків по 10 об'єктів кожен
x_list = [x]*10
y_list = [y]*10
#створення великого списку з об'єктами всіх минулих списків
big_list = x_list+y_list
#перевірка
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")