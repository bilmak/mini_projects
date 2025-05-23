from bs4 import BeautifulSoup
import requests



def write_html_file(link, filename="dealmeble.html"):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    response = requests.get(link, headers=headers)
    response.raise_for_status()
    
    with open(filename, "w") as file:
        file.write(response.text)

def get_price_from_file(file_path):
    with open(file_path, "r") as file:
        html = file.read()

    page_parse = BeautifulSoup(html, 'html.parser')

    price_container = page_parse.find("div", class_="current-price")
    if price_container:
        price_tag = price_container.find("span", attrs={"content": True})
        if price_tag:
            price = price_tag["content"]
        else:
            print("not found <span itemprop='price'>")
    else:
        print("not found <div class='current-price'>")
        
    
    
    return price

link = "https://dealmeble.pl/narozniki/naroznik-piecioosobowy-pikowany-glamour-chesterfield-kalifornia-2e2"
html_file = "dealmeble.html"

write_html_file(link)
price= get_price_from_file("dealmeble.html")
if price:
    print(f"Price: {price} zł")