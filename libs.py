import uuid

class Employee:
    def __init__(self, full_name, role, department, salary):
        self.id = str(uuid.uuid4())
        self.full_name = full_name
        self.role = role
        self.department = department
        self.salary = salary
        self.on_leave = False

    def go_on_leave(self):
        self.on_leave = True
    
    def return_from_leave(self):
        self.on_leave = False
    
    def __repr__(self):
        return f"Employee: {self.id} {self.full_name} {self.role} {self.department} {self.salary} {self.status} {self.on_leave}"