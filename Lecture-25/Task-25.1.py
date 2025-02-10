from abc import ABC, abstractmethod


class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine is now ON")

    def turn_off(self):
        print("Washing machine is now OFF")

class Refrigerator(Appliance):
    def turn_on(self):
        print("Refrigerator is now ON")

    def turn_off(self):
        print("Refrigerator is now OFF")

# ჩართვა-გამორთვის ფუნქცია
def operate_appliance(appliance: Appliance):
    appliance.turn_on()
    appliance.turn_off()

def main():
    washing_machine = WashingMachine()
    refrigerator = Refrigerator()

# გამოყენება
    operate_appliance(washing_machine)
    operate_appliance(refrigerator)




if __name__ == "__main__":
    main()
