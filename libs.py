import uuid

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.total_employee = 0
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        self.total_employee += 1

class OnLeave:
    def __init__(self, full_name, role):
        self.full_name = full_name
        self.role = role
        self.is_active = True

    def deactivate(self):
        self.is_active = False
        
    def activate(self):
        self.is_active = True

class Employee:
    def __init__(self, full_name, role, salary, bonus_hire, years_exp, department, location):
        self.id = str(uuid.uuid4())
        self.full_name = full_name
        self.role = role
        self.salary = salary
        self.bonus_hire = bonus_hire
        self.years_exp = years_exp
        self.department = department
        self.location = location
        self.employees = []

    def register_employee(self, on_leave: OnLeave, department: Department):
        self.department.add_employee(department)
        self.employees.append(on_leave)

    def get_on_leave_employees(self):
        on_leave_employees = []
        for employee in self.employees:
            if not employee.is_active:
                on_leave_employees.append(employee)
        return on_leave_employees
    
    def __repr__(self):
        return f"{self.full_name}, {self.role}, {self.salary}, {self.bonus_hire}, {self.years_exp}, {self.department.department_name}, {self.location}"