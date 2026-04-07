def zero_check(num):
    if num == 0:
        return "Number is Zero."
    else:
        pass

def factor_check(num):
    factors = []
    for n in range(1, num+1):
        if num % n == 0:
            factors.append(n)
    return factors

def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False

def prime_check(num):
    if len(factor_check(num)) > 2:
        return False
    else:
        return True
    
def square_find(num):
    return num ** 2

def cube_find(num):
    return num ** 3

n = 0
print(zero_check(n))
print(factor_check(n))
print(even_check(n))
print(prime_check(n))
print(square_find(n))
print(cube_find(n))