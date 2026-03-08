message = input(">")
words = message.split(" ")
emojis = {
    ":)": "🙂",
    ":(": "🙁",
}
for word in words:
    emojis.get(word, word)
print(output)