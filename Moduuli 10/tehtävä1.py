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

def main():
    lowest = 1
    highest = 10
    elevator = Elevator(lowest, highest)

    current_floor = 5
    elevator.move_to_floor(current_floor)

    elevator.move_to_floor(lowest)

if __name__ == "__main__":
    main()



