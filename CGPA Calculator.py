print("THIS IS CGPA CALCULATOR BASED ON CLASS MEAN AND DEVIATION")

from math import sqrt
no_of_students=int(input("enter number of students"))

marks=0
marks_stored=[]
#this is where teacher will input all the students marks
for i in range(no_of_students):
    mark=float(input(f"enter marks of student {i+1} \n"))
    marks_stored.append(mark)
    marks=marks+mark

print("**********************************")
final_marks=marks
print(f"NOTE 1:accumulative marks of the class is {round(final_marks,2)}")
mean=marks/no_of_students
print(f"NOTE 2:the mean of the clss is {round(mean,2)}")

square_deviation=0
for i in range(no_of_students):
    mean_deviation=(marks_stored[i]-mean)
    square_deviation+=(mean_deviation*mean_deviation)


standard_deviation=sqrt((square_deviation)/(no_of_students-1))
print(f"NOTE 3:the standard deviation of the clss is {round(standard_deviation,2)}")

#print(f"standard deviation is {standard_deviation}")

print("************************************")

print("CALCULATOR TO GUESS YOUR CGPA")
76

calculator_on==True
while calculator_on:
your_marks=float(input("enter your marks to know the cgpa"))
if your_marks>=(mean+(1.5*standard_deviation)):
    print(f"congratulations, your cgpa is S")
elif your_marks>=(mean+(0.5*standard_deviation)) and your_marks<(mean+(1.5*standard_deviation)):
    print(f"congratulation, your cgpa is A")
elif your_marks>=(mean-(0.5*standard_deviation)) and your_marks<(mean+(0.5*standard_deviation)):
    print(f"you can do better, your cgpa is B")
elif your_marks>=(mean-(1.0*standard_deviation))and your_marks<(mean-(0.5*standard_deviation)):
    print(f"you need to  do better, your cgpa is C")
elif your_marks>=(mean-(1.5*standard_deviation))and your_marks<(mean-(1.0*standard_deviation)):
    print (f"you need to  do better, your cgpa is D")
elif your_marks<(mean-(1.5*standard_deviation)):
    print(f"you didnt studied you cgpa is E")
else:
    print("sorry you failed, failed you need to give it again")



