while True:
    try:
        den = int(input("Vyberte den: "))
        break
    except ValueError:
        print("Nejedná se o číslo, zkus to znovu")
while True:
    if 1 <= int(den) <= 31:
        break
    den = input("Zkus to znovu, prosím vyber číslo od 1 do 31: ")
    if 1 <= int(den) <= 31:
        break

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

rok = 2014
a = (hello())
URL = "https://www.e-pocasi.cz/archiv-pocasi/"+ str(rok) +"/"+ str(den) +"-" + a +"/"
r = requests.get(URL)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek_2014=([span.text for span in td_tags][0])
n=2
vysledek_2014 = vysledek_2014[:-n or None]
print("V roce 2014 byla v Čechách průměrná teplota : " + vysledek_2014 + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
url_a= "https://www.e-pocasi.cz/archiv-pocasi/"+ str((int(rok) + 1)) +"/" + str(den) + "-" + a +"/"
r = requests.get(url_a)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek_2015=([span.text for span in td_tags][0])
n=2
vysledek_2015 = vysledek_2015[:-n or None]
print("V roce 2015 byla v Čechách průměrná teplota : " + vysledek_2015 + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
url_b= "https://www.e-pocasi.cz/archiv-pocasi/"+ str((int(rok) + 2)) +"/" + str(den) + "-" + a +"/"
r = requests.get(url_b)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek_2016=([span.text for span in td_tags][0])
n=2
vysledek_2016 = vysledek_2016[:-n or None]
print("V roce 2016 byla v Čechách průměrná teplota : " + vysledek_2016 + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
url_c= "https://www.e-pocasi.cz/archiv-pocasi/"+ str((int(rok) + 3)) +"/" + str(den) + "-" + a +"/"
r = requests.get(url_c)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek_2017=([span.text for span in td_tags][0])
n=2
vysledek_2017 = vysledek_2017[:-n or None]
print("V roce 2017 byla v Čechách průměrná teplota : " + vysledek_2017 + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
url_d= "https://www.e-pocasi.cz/archiv-pocasi/"+ str((int(rok) + 4)) +"/" + str(den) + "-" + a +"/"
r = requests.get(url_d)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek_2018=([span.text for span in td_tags][0])
n=2
vysledek_2018 = vysledek_2018[:-n or None]
print("V roce 2018 byla v Čechách průměrná teplota : " + vysledek_2018 + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
url_e= "https://www.e-pocasi.cz/archiv-pocasi/"+ str((int(rok) + 5)) +"/" + str(den) + "-" + a +"/"
r = requests.get(url_e)
# print(r.content)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

td_tags = soup.find_all("span", class_="topTemp")
vysledek_2019=([span.text for span in td_tags][0])
n=2
vysledek_2019 = vysledek_2019[:-n or None]
print("V roce 2019 byla v Čechách průměrná teplota : " + vysledek_2019 + "stupňů")
print(30*"_")
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

print(30*"_")
list1 = [vysledek_2014,vysledek_2015,vysledek_2016,vysledek_2017,vysledek_2018,vysledek_2019]
list2 = (int(vysledek_2014) + int(vysledek_2015) + int(vysledek_2016) + int(vysledek_2017) + int(vysledek_2018) + int(vysledek_2019))/len(list1)
print("Průměr teplot je: ", round((int(list2)),2) , "stupňu Celsia")

