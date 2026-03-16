# creating a resuable function

def emojiConvertor(message):
    emojies = {
        ":)": "🙂",
        ":(": "🙁"
    }
    words = message.split(" ")
    output = ""
    for word in words:
        output += emojies.get(word, word) + " "
    return output

message = input("> ")
print(emojiConvertor(message))

# Solution

#   def emoji_convertor(message):
#       words = message.split(" ")
#       emojis = {
#           ":)": "🙂",
#           ":(": "🙁",
#       }
#       output = ""
#       for word in words:
#           output += emojis.get(word, word) + " "
#       return output

#   message = input("> ")
#   print(emoji_convertor(message))