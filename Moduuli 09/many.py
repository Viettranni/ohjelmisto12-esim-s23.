import random
def cars():
    car_list = []
    for i in range(10):
        registration_number = f"ABC-{i+1}"
        top_speed = random.randint(100, 201)
        speed = random.randint(-10, 15)
        car_list.append((registration_number, top_speed, speed))

    return car_list

def main():
    car_list = cars()

    for registration in car_list:
        registration_number, top_speed, speed = registration
        print(f"Rekisterinumero: {registration_number}, Satunnainen nopeus: {top_speed}, Nopeus: {speed}")

main()