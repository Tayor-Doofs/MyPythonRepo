##########################################################################################################################
####################                            OBJECT ORIENTED PROGRAMMING                           ####################

class Employee:

    name = "Ade"
    age = 23
    salary = 230000

    def get_salary(self):

        return self.salary

new_employee = Employee()                               # instance or object creation
print(new_employee.name)
print(new_employee.get_salary())

class Admin(Employee):                                  # Admin employee inheriting from Employee
    name = "Kunle"
    designation = "Human resources"
    vat = 0.05
    pass

    def get_salary(self):
        return(self.salary *1.5) - (self.salary*self.vat)

second_employee = Admin()                               # instance or object creation
print(second_employee.name)
print(second_employee.designation)
print(second_employee.get_salary())
