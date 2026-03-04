# Car Game

cmd = input(">")
i = 0
while i == 0:
    if cmd == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
        cmd = input(">")
    elif cmd == "start":
        print("Car started...Ready to go!")
        cmd = input(">")
    elif cmd == "stop":
        print("Car stopped.")
        cmd = input(">")
    elif cmd == "quit":
        break
    else:
        print("I don't undertand that...")
        cmd = input(">")