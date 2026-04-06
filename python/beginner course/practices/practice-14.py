n = 16
count = 0

while count < 0:
    guess = int(input('Guessed Number: '))
    count += 1
    if guess == n:
        print('Congratulations, you guessed right!')
        break
else:
    print('Sorry you failed.')