# Переписать код в соответствии с Single Responsibility Principle:
# Подсказка: вынесите метод calculateNetSalary() в отдельный класс

class Employee:
    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob.strftime('%d.%m.%Y')
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"


class CalculateNetSalary:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_net_salary(self):
        tax = int(self.base_salary * 0.25)  # рассчитать налог другим способом
        return self.base_salary - tax
