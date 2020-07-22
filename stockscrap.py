import requests
import pandas as pd
import datetime 
from bs4 import BeautifulSoup

def live_market (stock):

    url2 = ('https://finance.yahoo.com/quote/')+stock+('?p=')+stock+('&.tsrc=fin-srch')
    res = requests.get(url2)

    webcont = BeautifulSoup(res.text,'lxml')
    webcont= webcont.find('div', {"class":'My(6px) Pos(r) smartphone_Mt(6px)'})

    webcont = webcont.find('span',class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)").text
    return webcont


lst=['MRF.NS','RELIANCE.BO','TATASTEEL.NS','ASHOKLEY.NS']

for step in range(1,101):
    price=[]
    col=[]
    timestamp= datetime.datetime.now()
    timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    for stk in lst :
        price.append(live_market(stk))
    col =[timestamp]
    col.extend(price)
    df =pd.DataFrame(col)
    df= df.T
    df.to_csv('C:\\Users\\avime\\Desktop\\PROJECTS\\Web Scrapping\\realmarket.csv',mode='a',header=False)   
    print(col) 
