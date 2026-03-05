# TYPE CONVERSION

totalMarks = int(input("Total Marks: "))
obtainedMarks = int(input("Obtained Marks: "))
deductedMarks = totalMarks - obtainedMarks
percentage = int(obtainedMarks / totalMarks * 100)
print(f"Deducted Marks: {deductedMarks}")
print(f"Percentage: {percentage}%")