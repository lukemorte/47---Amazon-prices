# 47 Amazon Prices

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

WEB_URL = "https://appbrewery.github.io/instant_pot/"
MAIL_SMTP = "seznam.smtp.cz"
MAIL_EMAIL = os.getenv("SEZNAM_EMAIL")
MAIL_PASSWORD = os.getenv("SEZNAM_PASSWORD")

HTTP_HEADER = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

response = requests.get(url=WEB_URL, headers=HTTP_HEADER)
html = response.text
html_data = BeautifulSoup(html, features="html.parser")

