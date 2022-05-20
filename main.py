import random
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

page = 1

file = open('catToys.csv', 'w', newline='\n')
f_obj = csv.writer(file)
f_obj.writerow(['Toy name', 'Pieces', 'Price', 'Product link'])


while page < 20:
    url = 'https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.63262d8f2aUo2L&IndexArea=product_en&SearchText=cat_toys&page=' + str(
        page )
    r = requests.get( url )
    soup = BeautifulSoup( r.text, "html.parser" )
    s = soup.find( 'div', class_='organic-list' )
    sub_soup = s.findAll( 'div', class_='J-offer-wrapper' )


    for each in sub_soup:

        name = each.h2.attrs.get('title')
        pieces = each.find( 'span', class_='element-offer-minorder-normal__value' ).text
        prod_link = each.find('a', class_='list-no-v2-left__img-container').attrs.get('href')
        price = each.find( 'span', class_='elements-offer-price-normal__price' )
        if price == None:
            price = "None"
        else:
            price = each.find( 'span', class_='elements-offer-price-normal__price' ).text

        print(price)
        f_obj.writerow([name, pieces, price, prod_link])


    page += 1
    dilay = random.randint(15, 20)
    sleep( dilay )
