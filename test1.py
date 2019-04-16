from bs4 import BeautifulSoup
import csv
import requests
"爬取薪资、经验、职位、位置"
html = open("test.html").read()
soup = BeautifulSoup(html,"lxml")
salary = soup.find("div",class_="cn").find("strong").text
post = soup.find("div",class_="cn").find("h1").text
txt = soup.find(class_="msg ltype").text.strip()
c_txt = txt.replace("|",",")
t_txt = salary + "," + post +","  + c_txt
d_txt = "".join(t_txt.split())
e_txt = d_txt + "\n"
with open("test.csv","w",encoding="utf-8") as f:
    f.write(e_txt)
    f.write(e_txt)
    f.close()
