import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

def scrape_title(url):
    # Set correct path for chromedriver
    chrome_driver_path = os.path.join(os.getcwd(), "chromedriver")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    title = driver.title
    driver.quit()
    return title

st.title("Chrome Web Scraping with Selenium")

url = st.text_input("Enter URL:")
if st.button("Scrape"):
    if url:
        st.write("Scraping title from:", url)
        try:
            title = scrape_title(url)
            st.write("Title:", title)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a URL.")
