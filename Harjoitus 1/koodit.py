# Tehtävä 1
import time
print("Hello World!")
time.sleep(10)

print("Python ")
time.sleep(1)
print("on ")
time.sleep(1)
print("kivaa ")
time.sleep(1)
print("ja ")
time.sleep(1)
print("helppoa.")
time.sleep(1)

# Tehtävä 2
a = 1
b = 3
print(a + b)

sana1 = "Python"
sana2 = "on"
sana3 = "helppoa"
sana4 = "ja"
sana5 = "kivaa"
sana6 = " "
print(sana1 + sana6 + sana2 + sana6 + sana3 + sana6 + sana4 + sana6 + sana5)

# Tulostessa ei ongelmaa, mutta laskutoimituksia tehdessä törmää TypeMiscmatchiing

# Tehtävä 3
nimi = input("Syötä nimesi: ")
print("Hei, + " + nimi)

n1 = int(input("Anna numero: "))
n2 = int(input("Anna toinen numero: "))
print("Summa on " + n1 + n2)

# Tehtävä 4
numero = input("Anna jokin numero: ")
numero = int(numero)
if numero > 10:
    print("Numerosi on yli 10")
elif numero < 10:
    print("Numerosi on alle 10")
else:
    print("Numerosi on tasan 10!")

print("E on ennen P:tä") if 'E' < 'P' else print("P onkin E:tä ennen...")

# Nelilaskin löytyy projekteista

# Tehtävä 5
i = 0
while i < 10:
    print("i on " + i)
    i += 1