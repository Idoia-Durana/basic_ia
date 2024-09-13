from bs4 import BeautifulSoup
import requests;

print("Version para BeautifulSoup:")
print("Version de request:", requests.__version__)

#1.Obtener el HTML

URL_BASE = 'https://www.eldulceobjetivo.com/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

#2.Parsear ese HTML

soup= BeautifulSoup(html_obtenido,"html.parser")

#Metodo find()

primer_h2 = soup.find('h2')
print(primer_h2)

#Sólo el texto
print(primer_h2.text)

#equivalente a:
print(soup.h2.text)

#find_all()
h2_todos=soup.find_all('h2')
print(h2_todos)

#ARGUMENTOS
#si usamos el aprametro limit=1, emilamos al metodo find
h2_uno_solo = soup.find_all('h2',limit=1)
print(h2_uno_solo)

# podemos iterara sobre un objeto
for seccion in h2_todos:
    print(seccion.text)

#podemos iterar sobre e lobjeto
for seccion  in h2_todos:
        print(seccion.text)

#get_text() para mas funcionalidades
for seccion in h2_todos:
    print(seccion.get_text(strip=True))

#Clase
divs=soup.find_all(class_= "heading-countainer heading-center")
for div in divs:
    print(div)
    print(" ")

#Todas las etiquetas que tengan el atributo src
src_todos=soup.find_all(src=True)