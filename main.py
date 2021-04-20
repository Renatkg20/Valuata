import requests 
from bs4 import BeautifulSoup
import re
from beautifultable import BeautifulTable

url = "https://valuta.kg/"
user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

source = requests.get(url, headers=user_agent, timeout= 2.50)

html_doc = source.text
# print(type(html_doc))
with open("index_txt.html", "w") as f:
    f.write(html_doc)

with open("index_txt.html", "r") as g:
  html = g.read()


html = html

soup = BeautifulSoup (html,'html.parser')
soup = soup.find("div", {"class": "kurs-bar__item"}).find_all("div", {"class": "rate-name"})


# for i in soup:
#   print(i.get_text())


soup = BeautifulSoup (html,'html.parser')
soup1 = soup.find("div", {"class": "container"})

fin1 = soup1.get_text()

# with open("valuta.txt", "w") as val:
#   val.write(fin1)
lis1 = [" ", "    ", "     ", "      ", "        ", "            "]
for q in lis1:
    fin2 = fin1.replace(f"{q}", "")





t = re.sub(r'\s+', ' ', fin2)
fin4 = t.split(" ")
# print(t)
# print(fin4)
# soup = soup.prettify()
# for a in soup:
#   print(a)
# lis1 = []

# for i in soup:
#     q = i.get_text()
#     w = q.replace("\n", " ")
#     w1 = w.replace("\t", " ")
#     lis1.append(w1)

# print(lis1)


#print(fin4[7:17])
h0=["Валюта"]
h1=[fin4[1],fin4[17], fin4[18]]
h2=[fin4[2],fin4[19], fin4[20]]
h3=[fin4[3],fin4[21], fin4[22]]
h4=[fin4[4],fin4[23], fin4[24]]
h5=[fin4[5],fin4[25], fin4[26]]
h6=[fin4[6],fin4[27], fin4[28]]
 
h0.append("Покупка")
h0.append("Продажа")

table = BeautifulTable()
table.column_headers = h0
table.column_headers = h0
table.append_row(h1)
table.append_row(h2)
table.append_row(h3)
table.append_row(h4)
table.append_row(h5)
table.append_row(h6)
#print(table)
final = table

with open("table.txt", "w") as r:
     r.write(str(final))

# from beautifultable import BeautifulTable


def valuta_kg():
  url = "https://valuta.kg/"
  user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
  source = requests.get(url, headers=user_agent, timeout= 2.50)
  html_doc = source.text
  soup = BeautifulSoup (html_doc,'html.parser')
  soup = soup.find("div", {"class": "container"})
  t = re.sub(r'\s+', ' ', fin2)
  fin4 = t.split(" ")

  # h0=["Валюта"]
  # h1=[fin4[1],fin4[17], fin4[18]]
  # h2=[fin4[2],fin4[19], fin4[20]]
  # h3=[fin4[3],fin4[21], fin4[22]]
  # h4=[fin4[4],fin4[23], fin4[24]]
  # h5=[fin4[5],fin4[25], fin4[26]]
  # h6=[fin4[6],fin4[27], fin4[28]]
 
  # h0.append("Покупка")
  # h0.append("Продажа")

  # table = BeautifulTable()
  # table.column_headers = h0
  # table.column_headers = h0
  # table.append_row(h1)
  # table.append_row(h2)
  # table.append_row(h3)
  # table.append_row(h4)
  # table.append_row(h5)
  # table.append_row(h6)
  # return (table)
  text_1 = " ".join(fin4[7:17])
  final_result = f"{text_1} \n\n | Валюта / Наличными |   Покупка  | Продажа \n\n | {fin4[1]} {fin4[17]} сом | {fin4[18]} сом | \n | {fin4[2]} {fin4[19]} сом | {fin4[20]} сом | \n | {fin4[3]} {fin4[21]} сом | {fin4[22]} сом | \n | {fin4[4]} {fin4[23]} сом | {fin4[24]} сом | \n | {fin4[5]} {fin4[25]} сом | {fin4[26]} сом | \n | {fin4[6]} {fin4[27]} сом | {fin4[28]} сом |"
  return final_result
print(valuta_kg())

def kicb_exch():
  url = "https://kicb.net/welcome/"
  user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
  source = requests.get(url, headers=user_agent, timeout= 2.50)
  html_doc = source.text
  soup = BeautifulSoup (html_doc,'html.parser')
  soup = soup.find("div", {"class": "con"})
  delete_space = re.sub(r'\s+', ' ', soup.get_text())
  split_space = delete_space.split(" ")
  fin4 = split_space
  final_result = f"Курс валюты в KICB наличный расчет \n\n | Валюта / Наличными | Покупка   |  Продажа \n\n |       {fin4[4]}          | {fin4[5]} сом | {fin4[6]} сом | \n |       {fin4[7]}          | {fin4[8]} сом | {fin4[9]} сом | \n |       {fin4[10]}          | {fin4[11]} сом | {fin4[12]} сом | \n |       {fin4[13]}          | {fin4[14]} сом | {fin4[15]} сом | \n " 
  # h0=["Валюта / Наличными"]
  # h1=[fin4[4],fin4[5], fin4[6]]
  # h2=[fin4[7],fin4[8], fin4[9]]
  # h3=[fin4[10],fin4[11], fin4[12]]
  # h4=[fin4[13],fin4[14], fin4[15]]
  # h0.append("Покупка")
  # h0.append("Продажа")

  # table = BeautifulTable()
  # table.column_headers = h0
  # table.column_headers = h0
  # table.append_row(h1)
  # table.append_row(h2)
  # table.append_row(h3)
  # table.append_row(h4)

  return final_result



print(kicb_exch())