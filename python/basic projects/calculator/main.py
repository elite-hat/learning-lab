def commandResponse():
    command = userInput
    match command:
        case "help":
            print('1. type "help" for more information')
            print("2. Write in a simple maths")
            print('3. Use real operators (type "operators" to list all supported operators)')
            print('4. Use predefined commands to control your calculator (type "commands" to list all supported commands)')
        case "quit":
            exit()
        case "commands":
            print('1. "help"\tTo get more information')
            print('2. "quit"\tTo exit the Calculator Program')
            print('3. "operators"\tTo list all supported operators')
            print('4. "commands"\tTo list al supported commands')
            print('5. "history"\tTo see your history')
            print('6. "reset"\tTo reset Calculation History')
        case "operators":
            print('"+"\tAdd')
            print('"-"\tSubtract')
            print('"*"\tMultiply')
            print('"/"\tDivide')
            print('"**"\tExponent')
            print('"//"\tFloor Division')
            print('"()"\tbrackets')
        case "history":
            if len(history) == 0:
                print("No history found")
            else:
                for recents in history:
                    print(recents)
        case "reset":
            history.clear()
            print("History Cleared")
def expressionResponse():
    expression = userInput
    try:
        result = eval(expression)
        print(result)
        history.append(f"{expression} = {result}")
    except:
        print("Math Error")
def process():
    if userInput in commandDictionary:
        commandResponse()
    elif all(char in expressionDictionary for char in userInput):
        expressionResponse()
    else:
        print("Syntax Error")

commandDictionary = ["help", "quit", "commands", "history", "reset", "operators"]
expressionDictionary = "1234567890 .-+*/()"
history = []
while True:
    userInput = input("> ")
    process()

# TODO: Add new features
# TODO: Support any case (upper or lower)