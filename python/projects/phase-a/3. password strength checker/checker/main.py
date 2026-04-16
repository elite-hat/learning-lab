from .data import numbers, lower_case, upper_case, symbols

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
    return score