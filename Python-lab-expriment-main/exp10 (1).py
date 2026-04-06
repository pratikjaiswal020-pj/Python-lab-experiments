
class Employee:
    def __init__(self):
        self.empid = None
        self.name = None
        self.basic_pay = 0.0
        self.ta = 0.0
        self.da = 0.0
        self.gross_pay = 0.0

    def input_details(self):
        self.empid = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.basic_pay = float(input("Enter Basic Pay: "))

    def calc(self):
        self.ta = 0.10 * self.basic_pay  
        self.da = 0.40 * self.basic_pay  
        self.gross_pay = self.basic_pay + self.ta + self.da

    def disp(self):
        print("\n--- Employee Details ---")
        print(f"Employee ID: {self.empid}")
        print(f"Name: {self.name}")
        print(f"Basic Pay: {self.basic_pay}")
        print(f"TA (10%): {self.ta}")
        print(f"DA (40%): {self.da}")
        print(f"Gross Pay: {self.gross_pay}")

emp = Employee()
emp.input_details()
emp.calc()
emp.disp()