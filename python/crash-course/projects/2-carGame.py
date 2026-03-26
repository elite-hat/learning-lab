# Car Game

cmd = input(">")
i = 0
start = False
while i == 0:
    if cmd == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
        cmd = input(">")
    elif cmd == "start":
        if start == False:
            start = True
            print("Car started...Ready to go!")
        else:
            print("Car is already started.")
        cmd = input(">")
    elif cmd == "stop":
        if start == True:
            start = False#
            print("Car stopped.")
        else:
            print("Car is already stopped.")
        cmd = input(">")
    elif cmd == "quit":
        break
    else:
        print("I don't undertand that...")
        cmd = input(">")