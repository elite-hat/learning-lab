title = 'palindrome checker'
print(title.upper())
word = input('Enter a word: ')
if word == word[::-1]:
    print(f"Yes! {word} = {word[::-1]}")
    print("So, it is a plaindrome.")
else:
    print('It is not a palindrome')