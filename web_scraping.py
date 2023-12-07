import requests
from bs4 import BeautifulSoup
import pandas as pd

titulo = list()
autor = list()
categoria = list()


url= 'http://127.0.0.1:8000/'
html_doc = requests.get(url)

soup= BeautifulSoup(html_doc.text,'html.parser')
# data=soup.find_all('td', attrs= {"class": "table-primary"})
# i=0
# #print(data)
# while(i+2<len(data)):
#     titulo.append(data[i].text)
#     autor.append(data[i+1].text)
#     categoria.append(data[i+2].text)
#     i+=3
#
#
#
# df = pd.DataFrame({'Titulos':titulo, 'Autores':autor, 'Categoria':categoria})
# df.to_csv(path_or_buf='personas.csv',index=False, encoding='utf-8')

tabla=soup.find('table')
filas=tabla.find_all('tr')

for fila in filas:
    celdas = fila.find_all('td')
    #print (celdas)

    if len (celdas)>0:
        titulo.append(celdas[0].string)
        autor.append(celdas[1].string)
        categoria.append(celdas[2].string)

#print(ancor)
#print(soup.prettify())
print(titulo)
print(autor)
print(categoria)

df = pd.DataFrame({'Titulos':titulo, 'Autores':autor, 'Categoria':categoria})
df.to_csv(path_or_buf='personas.csv',index=False, encoding='utf-8')