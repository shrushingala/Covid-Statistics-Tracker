from multiprocessing import connection
from multiprocessing.dummy import active_children
from time import strftime
from tkinter import *
import tkinter as tk 
from tkinter.font import Font
from turtle import heading
import urllib.request
from datetime import datetime
from click import confirm
from matplotlib.pyplot import figure, text, ylabel, xlabel,show
from seaborn import despine, barplot
from numpy import array
from pandas import DataFrame
from covid import Covid

root = Tk()
root.title("CF Covid Tracker")
root.geometry("600x450+500+150")

bluee = '#081D54'
root['bg'] = bluee

big_font = Font(family='Helvetica',size=40,weight='bold')
mid_font = Font(family='Helvetica',size=17,weight='bold')
small_font = Font(family='Helvetica',size=10,weight='bold')
textarea_font = Font(family='Rockwell',size=20,weight='bold')

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

test = connect()
connection = Label(bg=bluee,fg='white',pady=2)
connection.config(text=f'\nConnected: {test}',font=small_font)
connection.pack(fill=X)

heading = Label(text='CF Covid Tracker',font=big_font,bd=8,bg=bluee,fg='white',pady=1)
heading.pack(fill=X)

enter_country_name_label = Label(text='Enter country name',fg='white',bg=bluee,bd=8,pady=1)
enter_country_name_label.pack(fill= BOTH)

enter_country_name = Entry(root,font=textarea_font,justify='center')
enter_country_name.pack(pady=15)
enter_country_name.focus()


country =Label(root,bg=bluee,fg='white',font=mid_font)
country.pack()

confirms =Label(root,bg=bluee,fg='white',font=mid_font)
confirms.pack()

active =Label(root,bg=bluee,fg='white',font=mid_font)
active.pack()

death =Label(root,bg=bluee,fg='white',font=mid_font)
death.pack()

recovered =Label(root,bg=bluee,fg='white',font=mid_font)
recovered.pack()

last_updated = Label(root)

def plotGraph(dfn):
    ndf = dfn[['confirmed','active','death','recovered']]
    ndf = ndf.T
    figure(figsize=(5.5,5))
    for col in ndf.columns:
        pass
    plot = barplot(x=ndf.index,y=col,data=ndf)
    despine()
    for p in plot.patches:
        plot.annotate(format(p.get_height(),'1f',
                      p.get_x,p.get_width()/2.,p.get_height()),
                      ha ='center',va='center',
                      xytext = (0,9),
                      textcoords="offset points")

    xlabel = ('DATA')
    ylabel = ("COUNT")  
    show()              

def getData(country_name, country):
    if test:
        data = Covid()
        data = data.getData()
        df = DataFrame(data)
        country_name = country_name.get()
        dfn = df[country_name == df['country'].str.lower()]
        df = array(dfn)
        country_ = df[0][1]
        confirms_=df[0][2]
        active_=df[0][3]
        death_=df[0][4]
        recovered_=df[0][5]
        time_ = df[0][8]/1000
        last_updated_ = datetime.fromtimestamp(time_).strftime('%d-%m-%Y %H:%M:%S')
        print(last_updated_)

    country.configure(text=f"Country:{country_}")
    confirms.configure(text=f"Country:{confirms_}")
    active.configure(text=f"Country:{active_}")
    death.configure(text=f"Country:{death_}")
    recovered.configure(text=f"Country:{recovered_}")
    plotGraph(dfn)





root.bind('<Return>',(lambda x: getData(enter_country_name,country)))
PhotoImage(file='cf.png')
root.ic(False,pic)
root.mainloop()



