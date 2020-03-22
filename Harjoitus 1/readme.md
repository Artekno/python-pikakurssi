# Harjoitus 1

## Tehtävä 1: Varmista, että kaikki toimii ja helppo ohjelma.
- Avaa Visual Studio Code
- Luo uusi tiedosto
- Kirjoita `print("Hello World!")`
- Tallenna tiedosto nimellä helloWorld.py asianomaiseen kansioon
- Tuplaklikkaa tiedostoa kansiossa
- Tässä kohtaa tiedoston pitäisi vain nopeasti välähtää. Tämä johtuu siitä, että ohjelma suoritetaan heti ajamisen (eli tässä tapauksessa teksin näyttämisen jälkeen).
- Lisää koodiin seuraavat rivit:  
`import time`  
*print("Hello World!")*  
`time.sleep(10)`  

- Lisäämme tässä jo ensimmäisen kirjastomme, *time* n,joka tuo käytettäväksi mm. time.sleep(n) -komennon

**Uudet komennot:**  
- print("[TEKSTI]")
- time.sleep(n)

**Tehtävä**  
Tee ohjelma, joka tulostaa lauseen sana kerrallaan, sekunnin välein.
