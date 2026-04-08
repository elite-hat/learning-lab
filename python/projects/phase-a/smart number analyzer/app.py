from analyzer import factor_check, even_check, prime_check, square_find

n = int(input("Enter a number: "))

if n == 0:
    print("Number is Zero.")
else:
    factor_check(n)
    print("---")
    even_check(n)
    print("---")
    prime_check(n)
    print("---")
    square_find(n)