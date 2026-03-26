n = 16
count = 0
limit = 3

while count < limit:
    guess = int(input('Guessed Number: '))
    count += 1
    if guess == n:
        print('Congratulations, you guessed right!')
        break
else:
    print('Sorry you failed.')