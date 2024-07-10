from .Class import Class
from .Human import Human
from typing import List
from .Subject import Subject


class Teacher(Human):
    _homeroom_class: Class | None
    _subjects: List[Subject]

    def __init__(self, name, last_name, _subjects):
        super().__init__(name, last_name)
        self._subjects = list(_subjects)

    def set_class(self, cl: Class):
        if isinstance(cl, Class):
            self._homeroom_class = cl
            cl._homeroom_teacher = self
        else:
            raise Exception("Данный экземляр класса не найден")

    def get_class(self):
        return self._homeroom_class

    def __str__(self):
        return f'{self.name} {self.last_name}'

    def __repr__(self):
        return f'{self.name} {self.last_name}'
