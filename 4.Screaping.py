from bs4 import BeautifulSoup
import requests

url =r"C:\\Users\\idurana\\Desktop\\Python\\raw.html"
               
# Analizar sintácticamente el texto fuente HTML guardado en raw_html
html = BeautifulSoup(url, 'html.parser')
# Extraer el contenido de la etiqueta con la clase 'car-title' 
car_title = html.find(class_ = 'car-title').text.strip()
# Si el coche en cuestión resulta ser un Volkswagen Escarabajo
if (car_title == 'Volkswagen Escarabajo'):
    # Subir del título del coche a la siguiente etiqueta de elemento de lista <li></li>
    html.find_parent('li')
    
    # Determinar el precio del coche
    car_price = html.find(class_ = 'sales-price').text.strip()
    
    # Mostrar el precio del coche
    print(car_price)


