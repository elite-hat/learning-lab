subjects = ["Urdu", "English", "Mathematics", "Computer Science", "Physics", "Chemistry", "Fehm-ul-Qur'an", "Pakistan Studies"]

print(subjects)

print(subjects[0])      # first element
print(subjects[-1])     # last element
print(subjects[2])      # third element
print(subjects[-3])     # third last element

print(subjects[2:6])    # 3rd to 5th element
print(subjects[:6])     # first to 5th element
print(subjects[2:])     # 3rd to last element

subjects[-1] = "Pak Study"
print(subjects)