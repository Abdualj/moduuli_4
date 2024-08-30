# Vakio tuumien muuntamiseksi senttimetreiksi
TUUMA_CM = 2.54

while True:
    # pyydetään käyttäjältä tuumamäärä
    tuumat = float(input("Anna tuumamäärä (negatiivinen luku lopettaa):"))

    # Tarkistetaan, onko annettu luku negatiivinen
    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break

    #Muunnetaan tuumat sentimetreiksi
    senttimetrit = tuumat * TUUMA_CM
    print(f"{tuumat} tuumaa on {senttimetrit:.2f}.")



