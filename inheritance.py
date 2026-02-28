class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_manager(self):
        print("Department:", self.department)

    def give_bonus(self, bonus):
        self.salary += bonus
        print("Bonus added! New Salary:", self.salary)

m1 = Manager("Preeti", 30, 101, 50000, "IT")
m1.display_person()
m1.display_employee()
m1.display_manager()
m1.give_bonus(5000)