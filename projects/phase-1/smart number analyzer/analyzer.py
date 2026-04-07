def factor_check(num):
    factors = []
    for n in range(1, num+1):
        if num % n == 0:
            factors.append(n)
    return factors

def even_check(num):
    if num % 2 == 0:
        return True

def prime_check(num):
    if len(factor_check(num)) > 2:
        return False
    else:
        return True