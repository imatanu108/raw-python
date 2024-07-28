class Employee:
    def __init__(self, name, age, company, role):
        self.name = name
        self.age = age
        self.company = company
        self.role = role

    def offerJob(self, monthlySalary):
        print(f"Hello, {self.name}! Would you like to work for us @ ₹{monthlySalary}/month.")

    def getInfo(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Company : {self.company}")
        print(f"Role : {self.role}")


employee1 = Employee("Alex", 27, "Microsoft", "Backend Dev")

employee1.offerJob(240000)
employee1.getInfo()