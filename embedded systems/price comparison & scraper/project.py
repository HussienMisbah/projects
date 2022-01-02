from tkinter.constants import NONE
from bs4 import BeautifulSoup
import requests
import tkinter as tk
import webbrowser


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

flipkart='' 
ebay=''
amazon=''
olx=''

########################################### FOR VISIT BUTTON #################################################
def get_min() :

    try :
        label3 = tk.Label(root, text='minimum price :' + str(min_price) +'$')
    except :
        label3 = tk.Label(root, text='minimum price :' + 'not valid')
    label3.config(font=('helvetica', 12))
    canvas1.create_window(200, 550, window=label3)



def ebay_site():
    webbrowser.open(ebay) 
def FLipkart_site():
    webbrowser.open(flipkart) 
def amazon_site():
    webbrowser.open(amazon) 
def Olx_site():
    webbrowser.open(olx) 
def min_site():
    try :
        webbrowser.open(url_min) 
    except :
        return
################################################### GUI ###########################################################

def getProduct ():
    global name 
    name = entry1.get()
   # print(f"> {name}") 
    root.destroy()

root= tk.Tk()
root.title("user input")
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Welcome to Price comparison application !')
label1.config(font=('helvetica', 12))
canvas1.create_window(200, 50, window=label1)

label2 = tk.Label(root, text='Enter Product name:')
label2.config(font=('helvetica', 12))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 150, window=entry1)

button1 = tk.Button(text='submit',command=getProduct , bg='red', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 200, window=button1)

root.mainloop()

##################################################### WELCOME #######################################################

def gui() :
    global root
    global canvas1
    root= tk.Tk()
    root.title("Embedded systems GUI project")     # Add a title
    
    canvas1 = tk.Canvas(root, width = 800, height = 600)
    canvas1.pack()
    
    
    welome = "=> Welcome to Price comparison project <="
    label = tk.Label(root, text=welome)
    label.config(font=('Arial Bold', 16),foreground="blue")
    canvas1.create_window(400,30, window=label)
    
    
    label1 = tk.Label(root, text='Ebay' )
    label1.config(font=('Arial Bold', 14),foreground="blue")
    canvas1.create_window(50,70, window=label1)
    
    try :
        label2 = tk.Label(root, text='product Name :' +'  '+ ebay_name[:30] +'\n'+'price :'+ str(ebay_price)+'$')
    except :
         label2 = tk.Label(root, text='NOT FOUND')
    label2.config(font=('helvetica', 11))
    canvas1.create_window(300, 100, window=label2)
    
    
    
    button1 = tk.Button(text='visit site',command=ebay_site , bg='red', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(650, 100, window=button1)


    label1 = tk.Label(root, text='FLipkart' )
    label1.config(font=('Arial Bold', 14),foreground="blue")
    canvas1.create_window(70, 140, window=label1)
    try :    
        label2 = tk.Label(root, text='product Name :' +'  '+ flipkart_name[:30] +'\n' +'price :'+ str(flipkart_price)+'$')
    except :
        label2 = tk.Label(root, text='NOT FOUND')
    label2.config(font=('helvetica', 11))
    canvas1.create_window(300, 190, window=label2)
    
    button1 = tk.Button(text='visit site',command=FLipkart_site , bg='red', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(650, 190, window=button1)


    label1 = tk.Label(root, text='Amazon' )
    label1.config(font=('Arial Bold', 14),foreground="blue")
    canvas1.create_window(70, 240, window=label1)
    try :
        label2 = tk.Label(root, text='product Name :' +'  '+ amazon_name[:30] +'\n' + 'price :'+str(amazon_price)+'$')
    except :
        label2 = tk.Label(root, text='NOT FOUND')
    label2.config(font=('helvetica', 11))
    canvas1.create_window(300, 290, window=label2)
    button1 = tk.Button(text='visit site',command=amazon_site , bg='red', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(650, 290, window=button1)

    label1 = tk.Label(root, text='OLX' )
    label1.config(font=('Arial Bold', 14),foreground="blue")
    canvas1.create_window(50, 340, window=label1)

    
    try :
        label2 = tk.Label(root, text='product Name :' +'  '+ olx_name[:30] +'\n' +'price :'+ str(olx_price) +'$' )
    except:
        label2 = tk.Label(root, text='NOT FOUND')
    label2.config(font=('helvetica', 11))
    canvas1.create_window(300, 380, window=label2)
    
    button1 = tk.Button(text='visit site',command=Olx_site , bg='red', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(650, 390, window=button1)
    
    # min button :
    
    button1 = tk.Button(text='minimum_price',command=get_min, bg='green', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 500, window=button1)
    button1 = tk.Button(text='visit site of minimum ',command=min_site , bg='green', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(500, 500, window=button1)
    
    root.mainloop()

def main () :
    global  ebay_price , flipkart_price , amazon_price , olx_price
    ebay_price=ebay(name)
    flipkart_price=flipkart(name)
    amazon_price=amazon(name)
    olx_price = olx(name)
    

    if ebay_price == None or ebay_price == 0:
        ebay_price = "NOT FOUND"
    else:
        ebay_price = str(ebay_price[1:])
        ebay_price = int(float(str(ebay_price).replace(" ",'').replace(",",'').replace("$",'')))
      #  print("Ebay price: $",ebay_price,end= ' ')
       # print("Product name :",ebay_name)   


    if flipkart_price==None or flipkart_price == 0:
       # print("No product found!")
        flipkart_price = "NOT FOUND"
    else:
        flipkart_price=convert(flipkart_price)

    if amazon_price== None or amazon_price == 0:
        amazon_price = "NOT FOUND"
    else:
        amazon_price=convert(amazon_price)

    if olx_price ==None or olx_price ==0:
        olx_price = "NOT FOUND"
    else:
        olx_price=convert(olx_price)

    # get minimum 
    global min_price
    global url_min
    lst = [ebay_price,flipkart_price,amazon_price,olx_price]
    lst2=[]
    for j in range(0,len(lst)):
        if lst[j] != "NOT FOUND" and lst[j]>0:
            lst2.append(lst[j])
    if len(lst2) ==0 :
        gui()
        return
    else:
        min_price=min(lst2)
        price = {
            f'{ebay_price}':f"{ebay}",
            f'{amazon_price}':f'{amazon}',
            f'{olx_price}':f"{olx}",
            f'{flipkart_price}':f'{flipkart}'
        }
        for key, value in price.items():
            if int(key)==min_price:
                url_min= price[key]
    

    gui()


def flipkart(name):
    try:
        global flipkart
        global  flipkart_name
        name1 = name.replace(" ","+")   #iphone x  -> iphone+x
        flipkart=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)

       # print("\nSearching in flipkart....")
        soup = BeautifulSoup(res.text,'html.parser')
        flipkart_name = soup.select('._4rR01T')[0].getText().strip()  ### New Class For Product Name
        flipkart_name = flipkart_name.upper()
        if name.upper() in flipkart_name:
            flipkart_price = soup.select('._1_WHN1')[0].getText().strip()  ### New Class For Product Price
            flipkart_name = soup.select('._4rR01T')[0].getText().strip()
        else:
           # print("Flipkart:No product found!")
           # print("-----------------------")
            flipkart_price='0'
        return flipkart_price 
    except:
        flipkart_price= '0'
        return flipkart_price 

def ebay(name):
    try:
        global ebay
        global ebay_name
        name1 = name.replace(" ","+")
        url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0"
        res = requests.get(url)
        bs = BeautifulSoup(res.text,"html.parser")
       # print("\nSearching in ebay.....")
        
        for i in range(1,len(bs.select('.s-item__title')) ) :
            ebay_name = bs.select('.s-item__title')[i].getText().strip()
            name=name.upper()
            ebay_name=ebay_name.upper()
           
            if name in ebay_name or ebay_name in name :
                ebay_price = bs.select('.s-item__price')[i].getText().strip().split()[0]
                ebay_name = bs.select('.s-item__title')[i+1].getText().strip()
                ebay=url
                return ebay_price
    except:
        ebay_price = '0'
        return ebay_price

def amazon(name):
    try:
        global amazon
        global amazon_name
        name1 = name.replace(" ","-")
        name2 = name.replace(" ","+")
        amazon=f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)
       # print("\nSearching in amazon.....")
        soup = BeautifulSoup(res.text,'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0,amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in amazon_name[0:20]:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
                break
            else:
                i+=1
                i=int(i)
                if i==amazon_page_length:
                    amazon_price = '0'
                    break
        return amazon_price
    except:
     #   print("amazon: No product found!")
      #  print("-----------------------")
        amazon_price = '0'
        return amazon_price

def olx(name):
    try:
        global olx
        global olx_name
        name1 = name.replace(" ","-")
        olx=f'https://www.olx.in/items/q-{name1}?isSearchCall=true'
        res = requests.get(f'https://www.olx.in/items/q-{name1}?isSearchCall=true',headers=headers)
       # print("\nSearching in OLX......")
        soup = BeautifulSoup(res.text,'html.parser')
        olx_name = soup.select('._2tW1I')
        olx_page_length = len(olx_name)
        for i in range(0,olx_page_length):
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            name = name.upper()
            olx_name = olx_name.upper()
            if name in olx_name:
                olx_price = soup.select('._89yzn')[i].getText().strip()
                olx_name = soup.select('._2tW1I')[i].getText().strip()
                olx_loc = soup.select('.tjgMj')[i].getText().strip()
                try:
                    label = soup.select('._2Vp0i span')[i].getText().strip()
                except:
                    label = "OLD"
                break
            else:
                i+=1
                i=int(i)
                if i==olx_page_length:
                    olx_price = '0'
                    break
        return olx_price
    except:
        olx_price = '0'
        return olx_price

def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    k=f.replace("₹","$")
    g=int(float(k)/74.37)
    return g



main() 
