# 47 Amazon Prices

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

load_dotenv()

WEB_URL = "https://appbrewery.github.io/instant_pot/"
MAIL_SMTP = "smtp.seznam.cz"
MAIL_EMAIL = os.getenv("SEZNAM_EMAIL")
MAIL_PASSWORD = os.getenv("SEZNAM_PASSWORD")
MAIL_TO = "luke_py_test@yahoo.com"
TARGET_PRICE = 100


HTTP_HEADER = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}


def send_mail():
    with smtplib.SMTP(MAIL_SMTP) as connection:
        connection.starttls()
        connection.login(user=MAIL_EMAIL, password=MAIL_PASSWORD)

        msg = EmailMessage()
        msg.set_content(f"The price of the product on Amazon site went down of the treshold to {price}.")

        msg["Subject"] = "Amazon Price dropdown"
        msg["From"] = MAIL_EMAIL
        msg["To"] = MAIL_TO

        connection.send_message(msg)


# connection

response = requests.get(url=WEB_URL, headers=HTTP_HEADER)
html = response.text
soup = BeautifulSoup(html, features="html.parser")

# get the price

html_entity = soup.find(name="div", id="corePriceDisplay_desktop_feature_div")
price_number = html_entity.find(name="span", class_="a-price-whole").get_text()
price_fraction = html_entity.find(name="span", class_="a-price-fraction").get_text()
price = float(f"{price_number}{price_fraction}")

if price < TARGET_PRICE:
    send_mail()
