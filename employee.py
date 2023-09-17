import json
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
with open('employee.json', 'r') as file:
    data = json.load(file)
employees = []
for entry in data:
    employee = Employee(
        entry["Name"],
        entry["DOB"],
        entry["Height"],
        entry["City"],
        entry["State"]
    )
    employees.append(employee)
for employee in employees:
    print(f"Name: {employee.name}")
    print(f"DOB: {employee.dob}")
    print(f"Height: {employee.height} cm")
    print(f"City: {employee.city}")
    print(f"State: {employee.state}")
    print()
