emojis = {
    ":)" : "🙂",
    ":(" : "🙁"
}
message = input("Enter a message: ")
words = message.split(" ")
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)