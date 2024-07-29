from objects import Student, Teacher, Class, Subject, Human
import unittest


class Tests(unittest.TestCase):

    def setUp(self):
        # ниже создаём учеников, преподавателей и классы
        self.Alex = Student("Alexey", "Chernobrov")
        self.Petr = Student("Petr", "Ivanov")
        self.Michail = Student("Michail", "Belov")
        self.Svyat = Student("Svyatoslav", "Chernobrov")
        self.Anton = Student("Anton", "Egorov")
        self.Aleksandr = Student("Aleksandr", "Chernov")
        self.Maksim = Student("Maksim", "Nikolaev")
        self.Dmitry = Student("Dmitriy", "Andreev")
        self.Tatiana = Teacher("Tatiana", "Ryabchikova", [Subject.LIT, Subject.ART,
                                                          Subject.FOREIGN_LANG])
        self.Class1 = Class(self.Tatiana, [self.Alex, self.Aleksandr, self.Svyat, self.Dmitry, self.Petr,
                                           self.Michail, self.Anton])


    def test_set_grade_letter(self):  #проверка добавления буквы и цифры класса
        self.Class1.set_grade(10)
        self.Class1.set_letter("В")
        self.assertEqual(self.Class1._grade, 10)
        self.assertEqual(self.Class1._letter, 'В')

    def test_set_class(self):  #проверяем, что при присвоении класса ученику ученик также добавляется в класс
        self.Maksim.set_class(self.Class1)
        self.assertIn(self.Maksim, self.Class1._students)

    def test_new_student(self):  #проверяем, что при создании ученика с указанием класса ученик добавляется в класс
        Andrey = Student("Andrey", "Petrov", self.Class1)
        self.assertIn(Andrey, self.Class1._students)

    def test_append(self):
        Andrey = Student("Andrey", "Petrov")
        self.Class1.append(Andrey)
        self.assertIn(Andrey, self.Class1._students)

    def test_remove(self):
        self.Class1.remove(self.Anton)
        self.assertNotIn(self.Anton, self.Class1._students)

    def test_set_class_teacher(self): # проверяем смену класса для преподавателя
        Victor = Teacher("Victor", "Alekseev", [Subject.CHEMICS])
        Class3 = Class(self.Tatiana, [self.Petr, self.Michail, self.Anton])
        Victor.set_class(Class3)
        self.assertEqual(Victor._homeroom_class, Class3)

    def test_search(self): # тестируем поиск по подстроке
        self.assertEqual(self.Class1[''], self.Class1._students)
        # ниже заодно убеждаемся, что студенты внутри класса идут в алфавитном порядке сначала по фамилии, затем имени
        self.assertEqual(self.Class1['che'], [self.Alex, self.Svyat, self.Aleksandr])
        self.assertEqual(self.Class1['BE'], [self.Michail])

    def test_iter(self): # проверяем итерируемость
        self.assertEqual(self.Class1[2], self.Alex)
        self.assertEqual(self.Class1[0], self.Dmitry)
        self.assertEqual(self.Class1[-1], self.Petr)
        a = 0
        for elem in self.Class1:
            a += 1
        self.assertEqual(a, 7)

    def test_alph(self): #проверяем сравниваемость по алфавиту
        dl1 = self.Class1[0] < self.Class1[1]
        dl2 = self.Class1[1] < self.Class1[2]
        dl3 = self.Class1[2] < self.Class1[3]
        dl4 = self.Class1[5] < self.Class1[6]
        self.assertEqual(dl1, True)
        self.assertEqual(dl2, True)
        self.assertEqual(dl3, True)
        self.assertEqual(dl4, True)

