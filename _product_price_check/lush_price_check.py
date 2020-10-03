import requests
from bs4 import BeautifulSoup

request = requests.get("https://uk.lush.com/products/hair-treatments/hsuan-wen-hua")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("option", {"value": "25674"})
price_with_symbol = element.text.strip()
price = float(price_with_symbol[1:-7])
if price > 20:
    print("Probably better to wait for a price down")
else:
    print("Good price for a purchase!")
    print(f"The current price is £{price} ")