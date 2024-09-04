import random

# Tietokone arpoo kokonaisluvun väliltä 1..10
oikea_luku = random.randint(1, 10)

print("Tervetuloa numeronarvauspeliin!")
print("Olen arvannut luvun väliltä 1–10. Yritä arvata se.")

while True:
    # Pelaajalta pyydetään arvaus
    try:
        arvaus = int(input("Anna arvauksesi: "))

        if arvaus < oikea_luku:
            print("Liian pieni arvaus.")
        elif arvaus > oikea_luku:
            print("Liian suuri arvaus.")
        else:
            print("Oikein! Arvasit luvun oikein.")
            break  # Lopetetaan peli, kun arvaus on oikein

    except ValueError:
        print("Virheellinen syöte. Anna kokonaisluku väliltä 1–10.")

print("Kiitos pelaamisesta!")
