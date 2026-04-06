exam = {
    "subject" : "Computer Science",
    "total_marks" : 75,
    "has_practical" : True
}

print(exam["subject"])
#print(exam["theory_marks"])                This will give an error.
print(exam.get("theory_marks", "50"))     # This will assign a value of 50 to `theory_marks`, instead of giving an error.