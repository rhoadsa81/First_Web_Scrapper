from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url ='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#grabbing the webpage
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})
filename = "products.csv"
f = open(filename,"w")

headers = "brand, product_name\n"
f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    print("brand: "+ brand)
    print("Product: "+ product_name)

    f.write(brand + "," + product_name.replace(",","|") + "\n")
f.close()
