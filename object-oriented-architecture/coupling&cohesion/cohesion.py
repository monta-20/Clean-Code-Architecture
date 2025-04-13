# Low Cohesion (Bad) - Does unrelated things
class Employee:
    def calculate_salary(self): ...
    def send_email(self): ...       # Not related to core responsibility
    def generate_report(self): ...  # Should be in separate class

# High Cohesion (Good) - Focused responsibilities
class SalaryCalculator:
    def calculate(self): ...  # Only salary logic

class EmailService:
    def send(self): ...  # Only email logic