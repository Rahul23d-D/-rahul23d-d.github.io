class Student:
    def __init__(self, srn, name, marks):
        self.srn = srn
        self.name = name
        self.marks = marks

    def display(self):
        print("SRN:", self.srn)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("--------------------")


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)
    
    srn = input("Enter SRN: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    s = Student(srn, name, marks)
    students.append(s)

print("\nStudent Details")
print("====================")

for s in students:
    s.display()
