def zero_check(n):
    if n == 0:
        print(f"{n} is Zero.")
    else:
        print(f"{n} is not Zero.")
def negative_check(n):
    if n < 0:
        print(f"{n} is Negative.")
    else:
        print(f"{n} is Positive.")
def even_check(n):
    if n % 2 == 0:
        print(f"{n} is Even.")
    else:
        print(f"{n} is Odd.")
def square_check(n):
    for number in range(1, n+1):
        if number * number == n:
            print(f"{n} is a perfect square of {number}.")


def report(n):
    zero_check(n)
    negative_check(n)
    even_check(n)
    square_check(n)