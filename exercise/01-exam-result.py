"""
01. Write a program that takes a student's attendance % and marks, and prints DETAINED, PASS, or FAIL following the same rule order as the Exam Result case study.
"""

attendance = float(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))

if attendance < 75:
    print("DETAINED")
elif marks >= 40:
    print("PASS")
else:
    print("FAIL")