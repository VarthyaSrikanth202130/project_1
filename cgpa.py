def cgpaCalc(marks, n):
    grade = [0] * n
    Sum = 0
    for i in range(n):
       grade[i] = int((marks[i] / 10))
    for i in range(n):
       Sum += grade[i]
    cgpa = Sum / n
    return cgpa

def getGrade(avg):
    if avg>=91 and avg<=100:
        grade = "A1"
    elif avg>=81 and avg<91:
        grade = "A2"
    elif avg>=71 and avg<81:
        grade = "B1"
    elif avg>=61 and avg<71:
        grade = "B2"
    elif avg>=51 and avg<61:
        grade = "C1"
    elif avg>=41 and avg<51:
        grade = "C2"
    elif avg>=33 and avg<41:
        grade = "D"
    elif avg>=21 and avg<33:
        grade = "E1"
    elif avg>=0 and avg<21:
        grade = "E2"
    else:
        return -1
    return grade

print("To Calculate Result through subject marks-------ENTER 1")
print("To Calculate Percentage from Marks(total)-------ENTER 2")
print("To Calculate Percentage from CGPA---------------ENTER 3")
print("To Calculate  CGPA from Percentage--------------ENTER 4")
print("To Calculate  CGPA from Total Marks-------------ENTER 5")
print("To Calculate Total Marks from CGPA--------------ENTER 6")
print("To Calculate Total Marks From Percentage--------ENTER 7")

choice = int(input())
if choice == 1:
    marks = []
    total = 0
    n = int(input("Enter the number of subjects: "))
    print("Enter Marks Obtained in each subject: ")
    for i in range(n):
        marks.append(int(input()))
    print("Your entered marks of {} subjects are: {}".format(n,list(marks)))
    for i in range(n):
        total = total + int(marks[i])
    avg = total/n
    print("Yout grade is {}".format(getGrade(avg)))

    cgpa = cgpaCalc(marks, n)
    print("Your CGPA is: {}".format(cgpa))
    print("Your Percentage is = {}".format(cgpa * 9.5))
elif choice == 2:
    total_marks = int(input("Please Enter your Marks Obtaineds: "))
    max_marks = int(input("Please Enter Maximum marks: "))
    percentage = float((total_marks/max_marks)*100)
    print("Your Percentage is: {}".format(percentage))
elif choice == 3:
    cgpa = float(input("Please Enter your CGPA: "))
    percentage = float(9.5 * cgpa)
    print("Your percentage is: {}".format(percentage))
elif choice == 4:
    percentage = float(input("Please Enter your Percentage: "))
    cgpa = percentage/9.5
    print("Your CGPA is: {}".format(cgpa))
elif choice == 5:
    total_marks = int(input("Please Enter your Total Marks: "))
    max_marks = int(input("Please Enter your Maximum Marks: "))
    percentage = (total_marks/max_marks)*100
    print("Your CGPS is: {}".format(percentage*9.5))
elif choice == 6:
    cgpa = float(input("Please Enter your CGPA: "))
    max_marks = int(input("Please Enter your Maximum Marks: "))
    percentage = cgpa * 9.5
    total_marks = (percentage/100)*max_marks
    print("Your Total Marks are: {}".format(total_marks))
elif choice == 7:
    percentage = float(input("Please Enter your Percentage: "))
    max_marks = int(input("Please Enter your Maximum Marks: "))
    total_marks = (percentage/100)*max_marks
else: 
    print("Invalid Input")
