luku = int(input("Syötä kokonaisluku: "))
if luku <= 1:
    print(f"{luku} ei ole alkuluku.")
else:
    is_prime = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")