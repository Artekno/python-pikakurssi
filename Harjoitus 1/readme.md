# Harjoitus 1 - Peruskomennot

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

**Tehtävät**  
1. Tee ohjelma, joka tulostaa lauseen sana kerrallaan, sekunnin välein.


## Tehtävä 2: Muuttujat!
- Luo uusi tiedosto
- Luodaan kaksi muuttujaa ja asetetaan niille arvo: `a = 1` ja `b = 3`
- Huomaa: Python -kielessä muutujille ei normaalisti tarvise kertoa tiedostotyyppiä
- Tulostetaan muuttujien summa: `print(a + b)`

**Tehtävät**  
1. Tulosta lause, jossa jokainen sana tulostetaan eri muuttujana.
2. Mitä tapahtuu, jos suorittaa laskutoimitusta kahdelle *erityyppiselle* muuttujalle?


## Tehtävä 3: Käyttäjän syöte
- Luodaan muuttuja: `nimi`
- Asetetaan muuttujalle käyttäjän syöttämä nimi: `nimi = input("Syötä nimesi:")`
- Tulostetaan annettu nimi tervehdyksen kanssa: `print("Hei, " + nimi)`

**Uudet komennot**  
- input([SYÖTE])

**Tehtävät**  
1. Leiki inputin kanssa.

## Tehtävä 4: if-elif-else
- Kysytään käyttäjältä numeroa: `numero = input("Anna jokin numero:")`
- Muutetaan input **string**-tyypistä (lauseesta) **int**-tyyppiseksi (numeroksi): `numero = int(numero)`
- Tarkistetaan *if*-lausekkella, onko annettu numero yli: `if numero > 10:`
- Tee rivin vaihto, uuden rivin tulee alkaa sisennyksellä (yksi tab-painallus) ja kirjoita: `print("Numerosi on yli 10")`
- Tee uusi rivinvaihto, uuden rivin tulisi alkaa samalta tasolta *if*-lausekkeen kanssa. Kirjoita: `elif:`
- Uusi rivi alkaa taas yhdellä sisenyksellä: `print("Numerosi on alle 10")`
- Lopuksi luodaan *else*-ehto, jolla ei anneta ehtoja (ts. ehtona on, että kaikki if ja elif -lausekkeet ovat epätosia):  
`else:`  
    `print("Numerosi on tasan 10!")`
- Mikäli halutaan lisätä tarkasteluun lisää argumenttejä, voidaan käyttää && (and), sekä || (or) -komentoja
- Pelkät if-else lausekkeet voi laittaa tilan säästämiseksi samalle riville: `print("A") if a > b else print("B")`

**Uudet komennot:**  
- if-elif-else
- '<' (pienempikuin), '>' (suurempikuin), '==' (yhtäsuuri, älä käytä '=')
- '&&' (and/ja), '||' (or/tai)

**Tehtävät**  
1. Toista tehtävä käyttäen vertailussa kirjaimia tai tekstiä. Huomioi, että myös aakkosia voi vertailla: `a < b == tosi`
2. Tee yksinkertainen nelilaskin. Syötteen voidaan olettaa olevan kokonaislukuja.


## Tehtävä 5: while-loop
- Luodaan muuttuja i: `i = 0`
- Tehtään muuttujan avulla while-looppi: `while i < 10:`
- (Muista sisennys tuplapisteen jälkeisissä riveissä)
- Tulostetaan muuttujan arvo: `print("i on " + i)`
- Lisätään muuttujan arvoa yhdellä: `i = i + 1` tai `i += 1`
- Tulosteessa pitäisiä näkyä 10 kpl muuttujan arvoa

**Uudet komennot**
- while
- +=

**Tehtävät**  
1.
