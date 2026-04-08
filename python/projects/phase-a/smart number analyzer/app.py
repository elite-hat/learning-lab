from analyzer import factor_check, even_check, prime_check, square_find, cube_find

n = int(input("Enter a number: "))

def zero_check(num):
    if num == 0:
        return "Number is Zero."
    else:
        print(factor_check(n))
        print(even_check(n))
        print(prime_check(n))
        print(square_find(n))
        print(cube_find(n))