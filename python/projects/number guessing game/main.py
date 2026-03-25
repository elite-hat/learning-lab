import random
import time
title = 'number guessing game'
print(title.upper())
print('Enter a range of numbers:')
n1 = int(input('Starting number: '))
n2 = int(input('Ending number: '))
print('Computer is guessing a number...')
computer = random.randint(n1, n2)
time.sleep(1)
print('Done, Computer has choosen a number.')
print('Please, guess a number. (You have 3 lives)')
lives = 3
while lives > 0:
    user = int(input('> '))
    if user >= n1 and user <= n2:
        if user == computer:
            print(f'Congratulations!!! {user} is a correct number.')
            break
        else:
            lives -= 1
            print(f'Sorry! {user} is not the correct number, you have {lives} live(s) remaining.')
    else:
        print('Wrong Input')
else:
    print('Sorry, you have no lives left.')
    print(f'The correct answer is {computer}.')