class Employee:
    def __init__(self, emp_id, name, basic_salary):
        # Encapsulation (private variables)
        self.__emp_id = emp_id
        self.__name = name
        self.__basic_salary = basic_salary
        
        # Default percentages (can be modified easily)
        self.__hra_percent = 0.20   # 20%
        self.__da_percent = 0.10    # 10%
        self.__tax_percent = 0.15   # 15%

    # Method to calculate HRA
    def calculate_hra(self):
        return self.__basic_salary * self.__hra_percent

    # Method to calculate DA
    def calculate_da(self):
        return self.__basic_salary * self.__da_percent

    # Method to calculate Tax
    def calculate_tax(self):
        return self.__basic_salary * self.__tax_percent

    # Method to calculate Gross Salary
    def calculate_gross_salary(self):
        return self.__basic_salary + self.calculate_hra() + self.calculate_da()

    # Method to calculate Net Salary
    def calculate_net_salary(self):
        return self.calculate_gross_salary() - self.calculate_tax()

    # Display Payslip
    def display_salary_details(self):
        print("\n===== Employee Salary Details =====")
        print(f"Employee ID   : {self.__emp_id}")
        print(f"Name          : {self.__name}")
        print(f"Basic Salary  : {self.__basic_salary:.2f}")
        print(f"HRA           : {self.calculate_hra():.2f}")
        print(f"DA            : {self.calculate_da():.2f}")
        print(f"Tax Deduction : {self.calculate_tax():.2f}")
        print(f"Gross Salary  : {self.calculate_gross_salary():.2f}")
        print(f"Net Salary    : {self.calculate_net_salary():.2f}")
        print("===================================\n")


# ----------- Main Program -----------
if __name__ == "__main__":
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    emp = Employee(emp_id, name, basic_salary)
    emp.display_salary_details()
