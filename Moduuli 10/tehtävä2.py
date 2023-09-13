class Elevator:
    def __init__(self, lowest_floor, top_floor):
        self.floor = lowest_floor
        self.lowest_floor = lowest_floor
        self.top_floor = top_floor

    def floor_up(self):
        if self.floor < self.top_floor:
            self.floor += 1
        print(f"Hissi on kerroksessa {self.floor}")

    def floor_down(self):
        if self.floor > self.lowest_floor:
            self.floor -= 1
        print(f"Hissi on kerroksessa {self.floor}")

    def move_to_floor(self, current_floor):
        while self.floor != current_floor:
            if self.floor < current_floor:
                self.floor_up()
            elif self.floor > current_floor:
                self.floor_down()

class House:
    def __init__(self, lowest_floor, top_floor, elevator_amount):
        self.elevators = [Elevator(lowest_floor, top_floor) for _ in range(elevator_amount)]

    def drive_elevator(self, number_of_elevator, current_floor):
        if 0 <= number_of_elevator < len(self.elevators):
            self.elevators[number_of_elevator].move_to_floor(current_floor)
        else:
            print(f"Hissiä {number_of_elevator} ei löydy talosta. ")



def main():
    lowest = 1
    highest = 10
    number_of_elevators = 2
    house = House(lowest, highest, number_of_elevators)

    current_floor = 5
    house.drive_elevator(1, current_floor)

    current_floor = 3
    house.drive_elevator(1, current_floor)


if __name__ == "__main__":
    main()



