numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['~', '`', '-', '_', ':', ';', '.', ',', '(', ')', '{', '}', '[', ']', '?', '/', '|', '!', '@', '#', '$', '%', '^', '&', '*']

def check(password):
    score = 0
    lower_case_count = 0
    upper_case_count = 0
    numbers_count = 0
    symbols_count = 0
    for character in password:
        if character in lower_case:
            lower_case_count += 1
        if character in upper_case:
            upper_case_count += 1
        if character in numbers:
            numbers_count += 1
        if character in symbols:
            symbols_count += 1
    if lower_case_count > 0:
        score += 1
    if upper_case_count > 0:
        score += 1
    if numbers_count > 0:
        score += 1
    if symbols_count > 0:
        score += 1
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if lower_case_count > 1:
        score += 1
    if upper_case_count > 1:
        score += 1
    if numbers_count > 1:
        score += 1
    if symbols_count > 1:
        score += 1
    print(score)