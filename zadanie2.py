import os

nazwa = input("podaj nazwe folderu\n")
liczba = int(input("podaj liczbe podfolderow\n"))
n_pod = input("podaj nazwe podfolderow\n")

os.mkdir(nazwa)
os.chdir(nazwa)
for i in range(liczba):
    os.mkdir(f"{n_pod}_{i+1}")
