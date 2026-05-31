import csv
def total_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    total = basic + hra + da
    return total
f = open("employee.csv", "r")
r = csv.reader(f)
next(r)
for row in r:
    emp_id = row[0]
    name = row[1]
    basic_pay = float(row[2])
    salary = total_salary(basic_pay)
    print("Employee ID :", emp_id)
    print("Employee Name :", name)
    print("Basic Pay :", basic_pay)
    print("Total Salary :", salary)
    print()
f.close()
