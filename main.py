from lib import Student, Teacher, Class, Subject, Human



#ниже создаём учеников и преподавателей
Alex = Student("Alexey", "Chernobrov")
Petr = Student("Petr", "Ivanov")
print(Alex.get_class()) # проверка на None
Michail = Student("Michail", "Belov")
Svyat = Student("Svyatoslav", "Chernobrov")
Anton = Student("Anton", "Egorov")
Aleksandr = Student("Aleksandr", "Chernov")
Maksim = Student("Maksim", "Nikolaev")
Dmitry = Student("Dmitriy", "Andreev")
Tatiana = Teacher("Tatiana", "Ryabchikova", [Subject.LIT, Subject.ART, Subject.FOREIGN_LANG])
Anna = Teacher("Anna", "Mikhailova", [Subject.MATH, Subject.PHYSICS])
Victor = Teacher("Victor", "Alekseev", [Subject.CHEMICS])
Class1 = Class(Tatiana, [Maksim, Aleksandr, Svyat, Dmitry])
print(Class1) #выведет класс 0, но уже с преподавателем
Class1.set_grade(10)
Class1.set_letter("В")
Andrey = Student("Andrey", "Petrov", Class1)
Class2 = Class(Anna, [Petr, Michail, Anton])
Class2.set_grade(7)
Class2.set_letter("A")
Alex.set_class(Class1)
print(Alex.get_class()) #выводит класс данного студента с инфой
Tatiana.set_class(Class2) #проверяем смену класса для преподавателя
print(Tatiana.get_class())
print(Class1[""]) #проверяем работу поиска
print(Class1["Ch"])
print(Class2[2]) #проверяем обращение к Ученикам как к объектам списка
print(Class1[2])
print(Class1._students) # проверяем, как выглядит список учеников
Class3 = Class(Victor, []) #cоздаём класс с пустым списком учеников
Alexandr = Student("Alexandr", "Petrov", Class3) #создаём ученика, присвоив ему класс
print(Class3._students) #проверяем, добавился ли ученик в Учебный класс
for elem in Class1: #проверяем итерацию по сущности Class()
    print(elem.name, elem.last_name)
dl = Class1[2] < Class1[1] #проверка на сравниваемость по алфавиту
print(dl)
print(Human.ids) #принтуем айди всех созданных хьюманов
print({hash(Tatiana): 3}) #проверяем, чтобы хьюман мог быть хэшируемым
Class1.append(Anton) #проверяем работу append и remove с сущностью Class()
print(Class1._students)
Class1.remove(Anton)
print(Class1._students)

Class1.write_csv()
Class1.read_csv()