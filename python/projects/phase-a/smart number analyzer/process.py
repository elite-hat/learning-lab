def integer_check(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Positive"
    else:
        return "Zero"
    
def even_check(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def square_check(n):
    import math
    root = int(math.sqrt(n))
    if root*root == n:
        return f"Perfect square of {root}"
    else:
        return "not Perfect Square"
    
def factors_list(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return f"{len(factors)} factors = {factors}"

def prime_check(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    if len(factors) <= 2:
        return "Prime"
    else:
        return "not Prime"
    
def palindrome_check(int_n):
    str_n = str(int_n)
    if str_n == str_n[::-1]:
        return "Palindrome"
    else:
        return "not Palindrome"
    
# def report(n):
#     try:
#         print("\nREPORT")
#         print(f"\nNumber: {n}\n")
#         print(f"{n} is {integer_check(n)}")
#         print(f"{n} is {even_check(n)}")
#         print(f"{n} is {square_check(n)}")
#         print(f"{n} is {prime_check(n)}")
#         print(f"{n} is {palindrome_check(n)}")
#         print(f"{n} has {factors_list(n)}")
#         print("\n")
#     except ValueError:
#         print("Invalid Input")

def results(n):
    results = {
        "integer" : print(f"{n} is {integer_check(n)}"),
        "even" : print(f"{n} is {even_check(n)}"),
        "square" : print(f"{n} is {square_check(n)}"),
        "prime" : print(f"{n} is {prime_check(n)}"),
        "palindrome" : print(f"{n} is {palindrome_check(n)}"),
        "factors" : print(f"{n} has {factors_list(n)}")
    }
    return results

def report(n):
    try:
        print("\nREPORT")
        print(f"\nNumber: {n}\n")
        results(n)
        print("\n")
    except ValueError:
        print("Invalid Input")