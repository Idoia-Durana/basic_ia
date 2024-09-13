from bs4 import BeautifulSoup as soup
import requests;

#Clase
divs=soup.find_all(class_= "image_wrapper")
for div in divs:
    print(div)
    print(" ")

#Todas las etiquetas que tengan el atributo src
src_todos= soup.find_all(src=True)

for elemento in src_todos:
    if elemento['src'].endswith[".jpg"]:
        print(elemento)

