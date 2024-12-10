import json

class Employee:
    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = int(salary)

class Department:
    def __init__(self, name, description, employees):
        self.name = name
        self.description = description
        self.employees = []

        for employee in employees:
            each_employee = Employee(surname = employee["name"], position = employee["position"], salary = employee["salary"])
            self.employees.append(each_employee)

    def average(self):
        if not self.employees:
            return 0
        return sum(employee.salary for employee in self.employees) / len(self.employees)

    def max(self):
        if not self.employees:
            return 0
        return max(employee.salary for employee in self.employees)

    def min(self):
        if not self.employees:
            return 0
        return min(employee.salary for employee in self.employees)

    def positions(self):
        position_count = {}
        for employee in self.employees:
            if employee.position in position_count:
                position_count[employee.position] += 1
            else:
                position_count[employee.position] = 1
        return position_count

def main():
    pass

    try:
        with open("Lecture-21/Departments.json", "r") as department_file:
            info = json.load(department_file)
    except FileNotFoundError:
        print("File not found")

    departments = []
    for key, dept_data in info.items():
        info = Department(dept_data['name'], dept_data['description'], dept_data['employees'])
        departments.append(info)

    for department in departments:
        print(f"დეპარტამენტი: {department.name}")
        print(f"აღწერა: {department.description}")
        print(f"საშუალო ხელფასი: {department.average():.2f}")
        print(f"მაქსიმალური ხელფასი: {department.max()}")
        print(f"მინიმალური ხელფასი: {department.min()}")
        print(f"პოზიციების რაოდენობები: {department.positions()}")
        print("\n")

if __name__ == "__main__":
    main()