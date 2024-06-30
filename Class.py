from typing import List
import csv

class Class(list):
    _grade: int
    _letter: str
    _students: List["Student"]
    _homeroom_teacher: "Teacher"

    def __init__(self, _homeroom_teacher, _students=None):
        super().__init__()
        self._homeroom_teacher = _homeroom_teacher
        self._students = _students
        self._grade = 0
        self._letter = ""

    def __iter__(self):
        self._students.sort(key=lambda x: x.name)
        self._students.sort(key=lambda x: x.last_name)
        yield from self._students

    def append(self, st: "Student"):
        self._students.append(st)

    def remove(self, st: "Student"):
        self._students.remove(st)

    def set_grade(self, x: int):
        self._grade = x

    def set_letter(self, x: str):
        self._letter = x

    def __str__(self):
        return f'Класс: {self._grade}{self._letter}, преподаватель: {self._homeroom_teacher}'

    def __repr__(self):
        return f'{self._grade}{self._letter}'

    def __getitem__(self, name1: str):
        self._students.sort(key=lambda x: x.name)
        self._students.sort(key=lambda x: x.last_name)
        if type(name1) is str:
            a = []
            for student in self._students:
                if student.name.lower().startswith(name1.lower()) or student.last_name.lower().startswith(
                        name1.lower()):
                    a.append(student)
                else:
                    pass
            if len(a) > 0:
                return a
            else:
                raise Exception("Ученики не найдены")

            # если нужно получить не сами экземпляры, а конкретно имена:
            #         a.append(_student.name)
            #         a.append(_student.last_name)
            #     else:
            #         pass
            # b = [i + " " + j for i, j in zip(a[::2], a[1::2])]
            # return b
        else:
            return self._students[name1]
        # для получения имени и фамилии экземпляра заменить верхнюю строчку на:
        #     return f'{self._students[name1].name} {self._students[name1].last_name}'

    def write_csv(self):
        with open('testlist.csv', mode='w') as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\r')
            writer.writerow(["Имя", "Фамилия"])
            writer.writerow([self._homeroom_teacher.name, self._homeroom_teacher.last_name])
            for st in self._students:
                writer.writerow([st.name, st.last_name])

    def read_csv(self):
        with open('testlist.csv') as f1:
            file_reader = csv.DictReader(f1, delimiter=',')
            count = 0
            for row in file_reader:
                if count == 0:
                    print(f'Преподаватель: {row["Имя"]} {row["Фамилия"]}', end='\n')
                    print("Список учеников:")
                    count += 1
                else:
                    print(f'{row["Имя"]} {row["Фамилия"]}', end='\n')
                    count += 1

            print(f'Общее количество учеников: {count - 1} человек.')