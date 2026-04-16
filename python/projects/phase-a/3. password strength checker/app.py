from checker.main import check

print("\nPASSWORD STRENGTH CHECKER")

print("\nEnter a Password to check its strength.")

password = input("\nPassword: ")

check(password)

# Replace simple linear scoring with a weighted scoring system (different importance for length, variety, patterns, etc.)
# Add a penalty system to subtract points for weaknesses (sequences, repeats, common words)
# Improve pattern detection (detect sequential characters like 123, abc, and repeated characters like aaa)
# Implement strength classification (e.g., Weak / Medium / Strong based on score ranges)
# Improve feedback quality (give actionable suggestions, not just problem labels)
# Handle real-world weak cases (e.g., common passwords like “Password123” should score low despite meeting basic criteria)