class Employee :

    def work(self):
        print("Employee is Working")

class Developer(Employee) :

    def work(self):
        print("Developer is Working")

class Designer(Employee) :

    def work(self):
        print("Designe is Working")

class Manager(Employee) :

    def work(self):
        print("Designer is Working")


employees = [Developer(),Designer(),Manager()]

for employee in employees:
    employee.work()