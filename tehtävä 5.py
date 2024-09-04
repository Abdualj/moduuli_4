# Määritellään oikea käyttäjätunnus ja salasana
oikea_kayttajatunnus = "python"
oikea_salasana = "rules"

# Määritellään laskuri epäonnistuneille yrityksille
yritykset = 0
max_yritykset = 5

# Luodaan loop, joka pyytää kirjautumistietoja kunnes ne ovat oikein tai max_yritykset on saavutettu
while yritykset < max_yritykset:
    kayttajatunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana.")
        yritykset += 1

# Jos viisi yritystä on käytetty ilman onnistumista
if yritykset == max_yritykset:
    print("Pääsy evätty.")
