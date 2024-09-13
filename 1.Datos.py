import re
from colorama import Fore
import requests

website = "https://www.eldulceobjetivo.com/"
resultado = requests.get(website)
content = resultado.text
# print(content)

patron = r"/entry/[\w.]*"
maquinas_repetidas=re.findall(patron, str(content))
print(maquinas_repetidas)

sin_duplicados = list(set(maquinas_repetidas))
print(sin_duplicados)

maquinas_final=[]

for i in sin_duplicados:
    nombre_maquinas=i.replace("/entry/","")
    maquinas_final.append(nombre_maquinas)
    print(nombre_maquinas)

maquina_noob = "noob-1"
existe_noob=False

for a in maquinas_final:
    if a == maquina_noob:
        existe_noob=True
        break

color_verde = Fore.GREEN
color_amarillo = Fore.YELLOW


if existe_noob == True:
    print("\n"+ color_verde + "No hay ninguna máquina nueva")
else:
    print("\n"+ color_amarillo + "!Máquina  nueva!")
