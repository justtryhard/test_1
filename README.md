# Приложение для школы

Проект состоит из нескольких сущностей со своими атрибутами и методами. Описание классов следует ниже:

# Human

Сущность - Человек.
- Имеет атрибуты: name, last_name, __id, ids.
- Инициализируется атрибутами: name, last_name, __id (опционально).
- __id - уникальное значение, которое добавляется в атрибут ids (tuple). При передаче уже существующего значения возвращается ошибка. Если при инициализации поле оставить пустым - значение будет присвоено автоматически.
- Может сравниваться с другими сущностями по алфавитному порядку. 

# Student
Сущность - Ученик.
- Наследуется от Human.
- имеет те же атрибуты, что у Human, + _class (типа Класс).
- Инициализируется атрибутами: name, last_name, _class (опционально).
- При передаче атрибута _class в сущность типа Class (при её наличии) добавляется данный ученик.
- При вызове данной сущности возвращается имя, фамилия, класс, преподаватель.
- Имеет методы: get_class() - узнать, к какому классу относится ученик.
- set_class() - привязать ученика к классу (при наличии) - тут также данный ученик аппендится к списку сущности Class.

# Teacher
Сущность - Учитель.
- Наследуется от Human.
- имеет те же атрибуты, что у Humman, а также:
- _homeroom_class - класс (Class).
- _subjects - список предметов, которые ведёт данный преподаватель (List[Subject]).
- имеет методы get_class() и set_class(), которые работают аналогично как у Student.
- При вызове возвращает имя и фамилию.

# Subject
- Сущность наследуется от Enum.
- имеет несколько строковых атрибутов - предметы.

# Class
Сущность - Учебный класс.
- Наследуется от list.
- имеет атрибуты:
	- _grade - цифра класса (int), _letter - буква класса (str).
	- _students - список студентов (list["Student"]).
	- _homeroom_teacher - преподаватель "Teacher".
- Инициализируется передачей преподавателя и списка студентов (может быть None).
- Студенты внутри списка отсортированы по last_name. Если last_name совпадает, то по name.
- Изменены методы append() и remove() - теперь можно добавлять в _students сущности типа Student и также их удалять.
- методы set_grade() и set_letter() изменяют цифру и букву класса.
- При обращении по Class["ab"] выводятся все ученики, в имени или фамилии которых есть "ab", независимо от регистра. При отсутствии возвращает ошибку.
- Вывести всех учеников можно так: Class[""].
- При вызове Class[int] выводит ученика с переданным номером (по алфавитному порядку).
- При вызове Class() возвращает цифру и букву класса, а также преподавателя.
- Методы write_csv() и read_csv() создают и читают csv-файлы. В файл передаются и выводятся имена и фамилии преподавателя и учеников.

