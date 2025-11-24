#CGPA Calculator (Based on Class Mean & Standard Deviation)

This project is a simple Python program that calculates the class mean, standard deviation, and then predicts a student’s CGPA based on how far their marks deviate from the class average. It’s made to help teachers and students analyze performance in an easy and understandable way.

Features

Takes input for total number of students

Accepts individual marks of each student

Calculates:

Total class marks

Mean (average marks)

Standard deviation


Lets the user enter their own marks to estimate CGPA

Predicts CGPA using statistically defined ranges


How CGPA Is Predicted

The program uses the mean and standard deviation to decide your CGPA based on these ranges:

S Grade → Marks ≥ mean + 1.5 × SD

A Grade → Marks ≥ mean + 0.5 × SD

B Grade → Marks between −0.5 × SD and +0.5 × SD

C Grade → Marks between −1.0 × SD and −0.5 × SD

D Grade → Marks between −1.5 × SD and −1.0 × SD

E Grade → Marks < mean − 1.5 × SD


How to Run the Program

1. Install Python (if not already installed).


2. Download or clone this repository.


3. Run the script using:



python vit_grading.py

4. Follow the on-screen instructions.



Example Usage

Enter number of students

Enter each student’s marks

Program shows:

Total marks

Class mean

Standard deviation


Enter your own marks to know your CGPA


Purpose

This program is useful for:

Python beginners

Students preparing academic mini-projects

Teachers analyzing class performance

Anyone wanting a simple CGPA prediction tool


Future Improvements

Add GUI (Tkinter)

Support CSV or Excel input

Plot graphs of marks distribution

Export results automatically
