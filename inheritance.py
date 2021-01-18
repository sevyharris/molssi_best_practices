from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []
        self.id = self.generate_id()

    def generate_id(self):
        id_hash = 0
        for char in self.name:
            id_hash += ord(char)
        for char in self.surname:
            id_hash += ord(char)
        return id_hash % 10000000

    def __str__(self):
        return f'{self.surname}, {self.name}\nID: {self.id}\nCourses: {self.courses}'

    @abstractmethod
    def expertise(self):
        raise NotImplementedError


class Student(Person):
    def enroll(self, new_course):
        self.courses.append(new_course)

    def expertise(self):
        knowledge = 'Courses taken: '
        for course in self.courses:
            knowledge += f'{course},'
        return knowledge
    # def __str__(self):
    #    return f'{self.surname}, {self.name}\nCourses: {self.courses}'


class Faculty(Person):
    def __init__(self, name, surname, position, salary, degrees):
        # self.name = name
        # self.surname = surname
        self.position = position
        self.salary = salary
        self.courses = []
        self.degrees = degrees
        super().__init__(name, surname)

    def assign_course(self, new_course):
        self.courses.append(new_course)

    def expertise(self):
        knowledge = 'Degrees: '
        for degree in self.degrees:
            knowledge += f'{degree},'
        knowledge += '\nCourses Taught: '
        for course in self.courses:
            knowledge += f'{course},'
        return knowledge

    def __str__(self):
        return super().__str__() + f'\nPosition: {self.position}\nSalary: {self.salary}'


student1 = Student("Sevy", "Harris")
print(student1)
faculty1 = Faculty("Ruth", "Harris", "professor", 1000000, ['marine biology'])
print(faculty1)
print(faculty1.expertise())