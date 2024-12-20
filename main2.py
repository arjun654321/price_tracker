import streamlit as st
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import time
import threading

def checkprice(url):
    page = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"})
    soup = BeautifulSoup(page.content, "html.parser")
    
    a = soup.find('span', {'class': 'pip-price__integer'})
    
    price = float(a.text.replace("₹", "").replace(",", ""))
    print("price=", price)
    return price

def notify(email_id, email_sent, password, url):
    SMTP_SERVER = "smtp.gmail.com"
    PORT = 587
    server = SMTP(SMTP_SERVER, PORT)
    server.starttls()
    server.login(email_id, password)
    subject = "Buy now!!"
    body = f"Dear user, \nProduct price has fallen !! \nBUY NOW !!\ncheck the link \n{url}"
    msg = f"Subject: {subject} \n\n{body}"
    server.sendmail(email_id, email_sent, msg)
    server.quit()
    print("mail sent")

def run(url, myprice, email_id, email_sent, password):
    while True:
        if checkprice(url) > myprice:
            notify(email_id, email_sent, password, url)
        time.sleep(60*60*24)

st.title("IKEA Price Tracker")

url = st.text_input("Type IKEA product URL:")
myprice = st.number_input("Set price:", min_value=0.0, value=15000.0)
email_id = st.text_input("Enter sender's email ID:")
email_sent = st.text_input("Enter receiver's email ID:")
password = st.text_input("Type password of sender's email ID:", type="password")

if st.button("Start Tracking"):
    threading.Thread(target=run, args=(url, myprice, email_id, email_sent, password)).start()
    st.success("Price tracking started in the background!")