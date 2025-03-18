print("\t INVERTIS UNIVERSITY")
print("\t  Student Marksheet")
print("Name : Sahil Khan")
print("ID : BC2024376")
print("Roll No  : 2410201629")
print("\t {SUBJECTS}")
p = int(input("Enter Your Physics Marks ="))
c = int(input("Enter Your Chemistry Marks ="))
m = int(input("Enter Your Math Marks ="))
e = int(input("Enter Your English Marks ="))
py = int(input("Enter Your Python Marks = "))
print("Total of All Marks : ",(p+c+m+e+py))
total = (p+c+m+e+py)
#percentage = (total/500*100)
print ("Percentage is = ",(total/500*100))
print("Average is = ", (500%total))
if total >=500:
    print("Grade : A")
elif total >=400:
    print("Grade : B")
elif total >=300:
    print("Grade : C")
else:
    print("Grade : F")
