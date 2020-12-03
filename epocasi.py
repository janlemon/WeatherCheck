rok = 2014
den = input("Vyberte den: ")

def hello():
    mesic = input("Vyberte měsíc: ")
    if int(mesic) == 1:
        a = "ledna"
        return a
    elif int(mesic) == 2:
        a = "unora"
        return a
    elif int(mesic) == 3:
        a = "brezna"
        return a
    elif int(mesic) == 4:
        a = "dubna"
        return a
    elif int(mesic) == 5:
        a = "kvetna"
        return a
    elif int(mesic) == 6:
        a = "cervna"
        return a
    elif int(mesic) == 7:
        a = "cervence"
        return a
    elif int(mesic) == 8:
        a = "srpna"
        return a
    elif int(mesic) == 9:
        a = "zari"
        return a
    elif int(mesic) == 10:
        a = "rijna"
        return a
    elif int(mesic) == 11:
        a = "listopadu"
        return a
    elif int(mesic) == 12:
        a = "prosince"
        return a
    else:
        print("Lze pouze zadat měsíc pouze v číselné řadě od 1 do 12, zkus to znovu")
        return hello()

import requests
from bs4 import BeautifulSoup


a = (hello())
URL = "https://www.e-pocasi.cz/archiv-pocasi/"+ str(rok) +"/"+ den +"-" + a +"/"
r = requests.get(URL)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek=([span.text for span in td_tags][0])
n=2
vysledek = vysledek[:-n or None]
print("V roce 2014 byla v Čechách průměrná teplota : " + vysledek + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
url_a= "https://www.e-pocasi.cz/archiv-pocasi/"+ str((int(rok) + 1)) +"/" + den + "-" + a +"/"
r = requests.get(url_a)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek_a=([span.text for span in td_tags][0])
n=2
vysledek_a = vysledek_a[:-n or None]
print("V roce 2015 byla v Čechách průměrná teplota : " + vysledek_a + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
url_b= "https://www.e-pocasi.cz/archiv-pocasi/"+ str((int(rok) + 2)) +"/" + den + "-" + a +"/"
r = requests.get(url_b)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek_b=([span.text for span in td_tags][0])
n=2
vysledek_b = vysledek_b[:-n or None]
print("V roce 2016 byla v Čechách průměrná teplota : " + vysledek_b + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
url_c= "https://www.e-pocasi.cz/archiv-pocasi/"+ str((int(rok) + 3)) +"/" + den + "-" + a +"/"
r = requests.get(url_c)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek_c=([span.text for span in td_tags][0])
n=2
vysledek_c = vysledek_c[:-n or None]
print("V roce 2017 byla v Čechách průměrná teplota : " + vysledek_c + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
url_d= "https://www.e-pocasi.cz/archiv-pocasi/"+ str((int(rok) + 4)) +"/" + den + "-" + a +"/"
r = requests.get(url_d)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek_d=([span.text for span in td_tags][0])
n=2
vysledek_d = vysledek_d[:-n or None]
print("V roce 2018 byla v Čechách průměrná teplota : " + vysledek_d + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
url_e= "https://www.e-pocasi.cz/archiv-pocasi/"+ str((int(rok) + 5)) +"/" + den + "-" + a +"/"
r = requests.get(url_e)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek_e=([span.text for span in td_tags][0])
n=2
vysledek_e = vysledek_e[:-n or None]
print("V roce 2019 byla v Čechách průměrná teplota : " + vysledek_e + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

print(30*"_")
print(vysledek_e)
#avg = sum{list1}/len{list1}
print(30*"_")
print(30*"_")
print("Průměr teplot je")