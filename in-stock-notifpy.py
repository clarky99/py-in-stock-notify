from selenium import webdriver
from twilio.rest import Client
import schedule
import time

def checkStock():
    client = Client("Get a Client from Twilio", "Get an API Key from Twilio")
    driver = webdriver.Chrome()
    # enter items link below
    driver.get("Your product URL")

    print(driver.title)
    body = driver.find_element("tag name", "body")
    text = body.text 

    # Check body to see whatever the out of stock message is.
    if "NOTIFY ME WHEN BACK IN STOCK" in text.upper():
        print("It's still not available.")
    else:
        print("It's in stock!")
        client.messages.create(to = "+youcellnumber", from_ = "+twilionumber", body = "Your <item> is available.") 

    driver.quit()   

schedule.every(15).minutes.do(checkStock)

# Keep the script running to execute scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)