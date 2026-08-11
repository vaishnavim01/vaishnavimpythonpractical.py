name=input("Enter Student Name:")

marks1=float(input("Enter First Subjects Marks:"))
marks2=float(input("Enter Second Subjects Marks:"))
marks3=float(input("Enter Third Subjects Marks:"))

total = marks1 +marks2+ marks3
average = total/3 
print("\n***Student Score-Card***\n")
print("Student Name:",name)
print("Subject 1:",marks1)
print("Subject 2:",marks2)
print("Subject 3:",marks3)
print("Total Marks:",total)
print("Average Marks:",format(average,".2f"))