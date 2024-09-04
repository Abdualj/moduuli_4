# Alustetaan muuttujat suurimmalle ja pienimmälle luvulle
pienin = None
suurin = None

while True:
    syote = input("Anna luku (tai paina Enter lopettaaksesi): ")

    if syote == "":
        break  # Lopetetaan syöttö, jos käyttäjä painaa Enteriä ilman lukua

    try:
        luku = float(syote)  # Muutetaan syöte luvuksi (hyväksytään myös desimaalit)

        # Päivitetään suurin ja pienin luku
        if pienin is None or luku < pienin:
            pienin = luku
        if suurin is None or luku > suurin:
            suurin = luku

    except ValueError:
        print("Virheellinen syöte, yritä uudelleen.")  # Jos syöte ei ole kelvollinen luku

# Tarkistetaan, onko lukuja syötetty ja tulostetaan tulokset
if pienin is not None and suurin is not None:
    print(f"\nSyöttämistäsi luvuista pienin on: {pienin}")
    print(f"Syöttämistäsi luvuista suurin on: {suurin}")
else:
    print("\nEt syöttänyt yhtään lukua.")
