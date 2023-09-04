def gallons_litroiksi(gallon):
    litra = gallon * 3.785
    return litra

def main():
    while True:
        gallon = float(input("Olet jenkeistä, etkä ymmärrä mitään litroista. Anna gallon määrä niin muutan sen sinulle litroiksi! "))

        if gallon <= 0:
            print("Kiitos ajastasi!")
            break
        else:
            litra = gallons_litroiksi(gallon)
            print(f"{gallon} gallonia on litroina: {litra:.2f}!")

main()
