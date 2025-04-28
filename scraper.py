# scraper.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
from base import BaseComponent

class Scraper(BaseComponent):
    def __init__(self, url_list, max_headings=20):
        self.url_list = url_list
        self.max_headings = max_headings
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def run(self):
        return self.scrape()

    def scrape(self):
        output = ""
        for url in self.url_list:
            self.driver.get(url)
            print(f"\nScraping website at {url}")

            try:
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
                )
            except:
                print("Timeout waiting for heading to load")

            html = self.driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            headings = soup.find_all(['h1', 'h2', 'h3'])
            print("Total headings found:", len(headings))
            
            for i, h in enumerate(headings):
                if i >= self.max_headings:
                    output += f"...Reached {self.max_headings} headings, stopping early...\n"
                    break
                text = re.sub(r'\s+', ' ', h.get_text()).strip()
                output += text + "\n"
        return output

    def quit(self):
        self.driver.quit()

    def save_output(self, filename, output):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(output)
