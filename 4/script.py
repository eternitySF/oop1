#Оголошення функції яка повертає список користі
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

#Функція створення речення з попередніми стрічками
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit
#Оголошення функції з циклом який виводить створене речення для кожного варіанту
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
#Виклик функції
name_the_benefits_of_functions()