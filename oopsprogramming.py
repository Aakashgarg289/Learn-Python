# INTRODUCTION
# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def print_details(self):
#         return  f"{self.name} Salary is {self.salary} and Role is {self.role}."

# aakash = Employee("Aakash", 5000, 23)
# rohan = Employee("Rohan", 1000, "Dev")
# print(Employee.no_of_leaves)
# rohan.no_of_leaves = 10         
# print(rohan.__dict__)
# print(Employee.no_of_leaves)
# print(rohan.print_details())
# print(aakash.print_details())
# print(aakash.salary)

# SINGLE INHERITANCE
# class Employee:
#     no_of_leaves = 10
#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
#     def print_details(self):
#         return f"The Name is {self.name} and Salary is {self.salary} and the role is {self.role}"

# class Programmer(Employee):
#     def __init__(self, name, salary, role, languages):
#         self.name = name
#         self.salary = salary
#         self.role = role
#         self.languages = languages
#     def print_details(self):
#         return f"The Name is {self.name} and Salary is {self.salary} and the role is {self.role} and the languages are {self.languages}"

# aakash = Employee("Aakash", 1000, "Programmer")
# rohan = Employee("Rohan", 2000, "Analyst")
# karan = Programmer("Karan", 4000, "Developer", ["Python", "C++"])
# print(karan.languages)

# CLASS METHODS
# class Employee:
#     no_of_leaves = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#     def print_details(self):
#         return f"{self.name} is a {self.role} and the salary is {self.salary}"
#     @classmethod
#     def change_no_of_leaves(cls, new_leaves):
#         cls.no_of_leaves = new_leaves
#     @classmethod
#     def from_str(cls, string):                                              # Alternative Constructor
#         return cls(*string.split("-"))
#         # params = string.split("-")
#         # return cls(params[0], params[1], params[2])
#     @staticmethod
#     def good(string):
#         return f"{string} is a good boy"

# aakash = Employee("Aakash", 5000, "Programmer")
# rohan = Employee("Rohan", 50000, "iOS Developer")
# karan = Employee.from_str("Karan-480-Student")
# aakash.change_no_of_leaves(300)
# print(karan.salary)
# print(aakash.name, aakash.salary)
# print(aakash.print_details())
# print(rohan.no_of_leaves)
# print(aakash.good("Harry"))

# INSTANCE VARIABLE AND CLASS VARIABLE + SUPER()
# class A:
#     var1 = "I am a class variable in class A"
#     def __init__(self):
#         self.var = "I am inside class A constructor"
#         self.var1 = "Instance var in class A"
#         self.special = "Special"

# class B(A):
#     var1 = "I am a class variable in class B"
#     def __init__(self):
#         super().__init__()
#         self.var = "I am inside class B constructor"
#         self.var1 = "Instance var in class B"

# a = A()
# b = B()
# print(b.var1)
# print(b.special)

# SETTER, DELETER AND PROPERTY DECORATORS
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@github.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if (self.fname and self.lname) == None:
            return "Email is not set. Please set it using setter."
        return f"{self.fname}.{self.lname}@codewithaakash.com"
    @email.setter
    def email(self, string):
        print("Setting Now...")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

aakash = Employee("Aakash", "Garg")
print(aakash.email)
aakash.fname = "US"
print(aakash.email)
aakash.email = "this.that@codewithaakash.com"
print(aakash.fname)
del aakash.email
print(aakash.email)