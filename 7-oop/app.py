class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Worker(Human):
    def __init__(self, name, age, salary):
        self.salary = salary
        super().__init__(name, age)


class Teacher(Worker):
    def __init__(self, name, age, salary, branch):
        self.branch = branch
        super().__init__(name, age, salary)

    def __str__(self):
        return (f"Teacher-> Name:{self.name} Age:{self.age} Salary:{self.salary}")


class Student(Human):
    def __init__(self, name, age, lessons):
        super().__init__(name, age)
        self.lessons = lessons

    def __str__(self):
        return (f"Student: {self.name} - {self.age}")


student1 = Student("Ahmet Kaya", 18, ["Fen bilgisi", "Coğrafya", "Matematik"])
teacher1 = Teacher("Ayşe Korucu", 45, 10000, "Coğrafya")

print(student1.__str__())
print(teacher1.__str__())

print(student1.name)
print(teacher1.name)
