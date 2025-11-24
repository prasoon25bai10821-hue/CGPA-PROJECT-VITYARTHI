This Python program is a CGPA Calculator that works based on the class mean and standard deviation.                                               
The idea is to create a grading method that adapts to the actual performance of the class instead of using fixed grade boundaries.

The teacher first enters the number of students and then inputs each student's marks. The program stores all marks, calculates:

Total marks of the class

Mean (average)

Standard deviation

Once these values are calculated, a student can enter their own marks, and the program will estimate their CGPA category based on how far their marks are from the class mean.

The grading scale used in the program is:

S Grade: your marks ≥ mean + 1.5 × SD

A Grade: between mean + 0.5 × SD and mean + 1.5 × SD

B Grade: between mean − 0.5 × SD and mean + 0.5 × SD

C Grade: between mean − 1.0 × SD and mean − 0.5 × SD

D Grade: between mean − 1.5 × SD and mean − 1.0 × SD

E Grade: marks below mean − 1.5 × SD


The program uses Python’s built-in math.sqrt() for standard deviation and simple conditional statements to decide the grade.

It is a straightforward and easy-to-run script meant for practicing Python, basic math functions, and simple statistical grading.
