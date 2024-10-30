class Helicopter:
    public_year = 2060
    public_model = "Default Model"

    def __init__(self, passenger_capacity=0, name="Unknown", max_speed=0):
        self.__passenger_capacity = passenger_capacity
        self.__name = name
        self.__max_speed = max_speed

    def get_passenger_capacity(self):
        return self.__passenger_capacity

    def get_name(self):
        return self.__name

    def get_max_speed(self):
        return self.__max_speed

    def __str__(self):
        return f"Passenger capacity = {self.__passenger_capacity}; Name = {self.__name}; Max speed = {self.__max_speed}"

    def __repr__(self):
        return f"Helicopter ({self.__passenger_capacity}; {self.__name}; {self.__max_speed})"

    def __del__(self):
        print(f"Helicopter {self.__name} destroyed")

def main():
    hel1 = Helicopter(20, "NB", 3000)
    hel2 = Helicopter(15, "RM", 2000)
    hel3 = Helicopter(10, "V", 1500)

    print(hel1)
    print(hel2)
    print(hel3)

    print(f"Public Fields: year - {Helicopter.public_year}, model - {Helicopter.public_model}")

if __name__ == "__main__":
    main()
