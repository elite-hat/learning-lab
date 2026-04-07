class Car:
    def start(self):
        car_started = True
        print("Car is started.")
    def stop(self):
        car_started = False
        print(" is stopped.")

class AutomaticCar(Car):
    def drive(self):
        print("Car is moving now.")
class ManualCar(Car):
    def drive(self):
        print("You have to drive it by your own.")

tesla = AutomaticCar()
tesla.start()
tesla.drive()
tesla.stop()

toyota = ManualCar()
toyota.start()
toyota.drive()
toyota.stop()