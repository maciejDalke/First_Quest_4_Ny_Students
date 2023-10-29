import requests #trzeba doinstalowac ta biblioteke w pycharmie

def rozne():
    odp = requests.get(url)
    cytaty = odp.json()
    a = cytaty['quote']
    while a in cyt:
        odp = requests.get(url)
        cytaty = odp.json()
        a = cytaty['quote']
    return a

url = "https://api.kanye.rest"

odp = requests.get(url)

cyt = []
if odp.status_code == 200:
    cytaty = odp.json()
    o = "Y"
    while o == "Y":
        a = rozne()
        cyt.append(a)
        print(a)
        o = input("\nkolejny???[Y/n] ")

else:
    print("Wystąpił błąd. Kod statusu:", odp.status_code)

