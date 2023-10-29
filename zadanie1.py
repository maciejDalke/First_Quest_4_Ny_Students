import os

def zmien(plik):
    zm = plik
    for i in range(zm.count(" ")):
        zm = zm.replace(" ", "_")
    os.rename(plik, zm)

pliki = os.listdir()

print(pliki)

while len(pliki) != 0:
    if pliki[0].count(" ") > 0:
        zmien(pliki[0])
    pliki = pliki[1:]