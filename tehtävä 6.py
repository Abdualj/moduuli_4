import random

def laske_pi_likiarvo(pisteiden_maara):
    ympyrassa_sisalla = 0

    for _ in range(pisteiden_maara):
        # Arvotaan piste (x, y) neliön B sisälle, jossa x ja y ovat välillä [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Tarkistetaan, onko piste yksikköympyrän sisällä (x^2 + y^2 < 1)
        if x**2 + y**2 < 1:
            ympyrassa_sisalla += 1

    # Piin likiarvo on 4 * (ympyrässä sisällä olevat pisteet / kaikki pisteet)
    pi_likiarvo = 4 * ympyrassa_sisalla / pisteiden_maara
    return pi_likiarvo

# Kysytään käyttäjältä pisteiden määrä
pisteiden_maara = int(input("Anna pisteiden määrä: "))

# Lasketaan piin likiarvo
pi_likiarvo = laske_pi_likiarvo(pisteiden_maara)

# Tulostetaan piin likiarvo
print(f"Piin likiarvo arvottujen pisteiden perusteella on: {pi_likiarvo}")
