title = 'palindrome checker'
print(title.upper())
word = input('Enter a word: ')
if word == word[::-1]:
    print(f"Yes! {word} is equal to {word[::-1]}")
    print("So, it is a plaindrome.")
else:
    print(f"No! {word} is not equal to {word[::-1]}")
    print("So, it is not a palindrome.")