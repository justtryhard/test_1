from Class import Class
from Human import Human


class Student(Human):
    _class: Class

    def __init__(self, name, last_name, _class=None):
        super().__init__(name, last_name)
        self._class = _class
        if isinstance(_class, Class):
            self._class = _class
            self._class.append(self)

    def set_class(self, cl: Class):
        if isinstance(cl, Class):
            self._class = cl
            cl.append(self)
        else:
            raise Exception("Данный экземляр класса не найден")

    def get_class(self):
        return self._class

    def __str__(self):
        return f'Ученик {self.name} {self.last_name}, {self._class}'

    def __repr__(self):
        return f'{self.name} {self.last_name}'
