Physics=float(input("enter the marks of Physics out of 100 "))
Chemistry=float(input("enter the marks of Chemistry out of 100 "))
Maths=float(input("enter the marks of Maths out of 100 "))
Hindi=float(input("enter the marks of Hindi out of 100 "))
English=float(input("enter the marks of English out of 100 "))
total_marks=Physics+Chemistry+Maths+Hindi+English
print("total marks obtained=",total_marks)
per=total_marks*100/500
print("percentage secured=",per)
if per>=60:
    print("first division")
elif per>=45:
    print("2nd division")
elif per>=33:
    print("3rd division")
else:
    print("fail")