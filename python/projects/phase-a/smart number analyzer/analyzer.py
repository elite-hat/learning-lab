def factor_check(num):
    global factors
    factors = []
    for n in range(1, num+1):
        if num % n == 0:
            factors.append(n)
    print("Factors:")
    for factor in factors:
        print(factor)

def even_check(num):
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

def prime_check(num):
    if len(factors) > 2:
        print(f"{num} is not Prime.")
    else:
        print(f"{num} is Prime.")
    
def square_find(num):
    print(f"{num} ^ 2 = {num**2}")