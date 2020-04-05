# Harjoitus 2 - Yksinkertaiset ohjelmat

## Tehtävä 6: Tähtien luonti
- Luodaan ohjelma, joka kysyy tähtien määrän (=rivien)
`n = int(input("How many stars?"))`
- Alkaen yhdestä tähdestä, ohjelma tulostaa seuraavalle riville yhden tähden
enemmän kuin edellisellä rivillä kunnes saavutetaan annettu tähtien määrä.
`for i in range(n):
    for j in range(i):
        print("*", end='')
    print("")`

**Tehätävät**
1. Ohjelma tulostaa ensin tähdet nousevassa järjestyksessä (kuten esimerkissä),
ja perään laskevassa järjestyksessä.
2. Töhdet tulostetaan joulukuusen muodossa (eli ns. keskitetysti)
