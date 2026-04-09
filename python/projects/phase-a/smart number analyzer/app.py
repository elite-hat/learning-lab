import process

n = int(input("Enter a number: "))

process.report(n)

# TODO:

# ❌ You did not meet core requirements fully
# ❌ Output design is weak
# ❌ Logic depth is incomplete

# Critical Misses (Important)
# ❌ Missing Required Features

# You were supposed to implement:

# Prime check ❌
# Palindrome check ❌
# Armstrong check ❌
# Factors ❌

# 👉 You implemented different checks instead:

# zero
# negative
# even
# square

# Problem:
# You changed the problem instead of solving it.

# In real engineering: this is a requirement failure, not a minor mistake.

# 3. Design Issues
# 1. Functions PRINT instead of RETURN

# Current:

# def even_check(n):
#     if n % 2 == 0:
#         print(...)

# Problem:

# Not reusable
# Not testable
# No control over output
# Correct approach:
# def even_check(n):
#     return n % 2 == 0

# 👉 Then format output in report()

# 2. Weak Report System

# Current:

# process.report(n)

# But it just prints line by line.

# Missing:

# Structured output
# Summary style
# 3. Square Check Inefficient
# for number in range(1, n+1):

# This is:

# O(n)
# unnecessary

# Better:

# import math
# root = int(math.sqrt(n))
# if root * root == n:
# 4. No Input Validation
# n = int(input(...))

# If user enters:

# abc

# → program crashes

# 4. What You Did Well
# ✅ Separation of files
# Good instinct → scalable design
# ✅ Function decomposition
# Each logic isolated → correct direction
# ✅ Clean syntax
# No clutter, readable
# 5. What You Should Fix (Version 2)
# Step 1 — Fix Requirements (NON-NEGOTIABLE)

# Add:

# is_prime(n)
# is_palindrome(n)
# is_armstrong(n)
# get_factors(n)
# Step 2 — Refactor Output Design
# def report(n):
#     results = {
#         "prime": is_prime(n),
#         "palindrome": is_palindrome(n),
#         "armstrong": is_armstrong(n),
#         "factors": get_factors(n)
#     }

#     return results

# Then print in app.py

# Step 3 — Add Input Safety
# try:
#     n = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input")
# 6. Strategic Feedback (Important)
# Your Behavior Pattern:

# You:

# Understood structure ✅
# Avoided core difficulty ❌

# This is dangerous long-term.

# Rule Going Forward

# Never modify the problem to make it easier.

# Always:

# Face the hardest part directly
# Even if slow
# 7. Final Judgment

# You showed:

# Good coding habits
# Weak problem adherence
# Next Step

# Do NOT move to Project 2.

# 👉 Fix this project first:

# Add missing features
# Refactor output
# Improve structure
