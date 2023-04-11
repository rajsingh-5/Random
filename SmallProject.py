from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r = requests.get(url)
Product_Name = []
Price_Name = []
Review_Star = []
Product_Details = []

soup = BeautifulSoup(r.text, "lxml")
for pageNo in range(2, 327):
    np = soup.find("a", class_="_1LKTO3").get("href")
    new_URL = "https://www.flipkart.com" + np.replace("page=2", f"page={pageNo}")
    new_Request = requests.get(new_URL)
    soup_N = BeautifulSoup(new_Request.text, "lxml")
    box = soup_N.find("div", class_="_1YokD2 _3Mn1Gg")
    product_name = box.findAll("div", class_="_4rR01T")
    for item in product_name:
        Product_Name.append(item.text)
    price_name = box.findAll("div", class_="_30jeq3 _1_WHN1")
    for item in price_name:
        Price_Name.append(item.text)
    review_star = box.findAll("div", class_="_3LWZlK")
    for item in review_star:
        Review_Star.append(item.text)
    product_details = box.findAll("div", class_="fMghEO")
    for item in product_details:
        if item.text is None:
            Product_Details.append("NULL")
        Product_Details.append(item.text)
print("Name", len(Product_Name))
print("Price", len(Price_Name))
print("Review", len(Review_Star))
print("Details", len(Product_Details))
df = pd.DataFrame({"Product_Name": Product_Name, "Prices": Price_Name, "Product_Details": Product_Details})
df.to_csv("Flipkart_Dummy.csv")
