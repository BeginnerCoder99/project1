#I've decided to use BeautifulSoup for the scrapeing with lxml as the parser
#first using pip install requests beautifulsoup4 lxml in cmd shell.
#double checked that created new branch and inside it for github.
#importing requests and re for HTTP requests and text cleaning
#It does appaear to be working, but having issues with sites
#using selenium as a website emulator to identify if website security or coding issue
#pip install --upgrade selenium
#not working, using pip install webdriver-manager
#I keep running into anti-bot protection on websites
#Found websites without bot protection
#Had to encode unicode to get around windows bug with txt files.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

options = webdriver.ChromeOptions()
options.add_argument('--headless')  
#website emulation but no browser cause headless

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


with open("url_list.txt") as file:
    url1 = file.readline()
    url2 = file.readline()
    url3 = file.readline()
urlList = [url1, url2, url3]
#reads first three then puts into array as urls

output = ""
#creates empty string
#for loop iterates through urlList array until done for each array
for x in urlList:
    driver.get(x)
    print("\nScraping website at", x)
    output += "\nScraping website at " + x 
    #had issue with one site not using headers but specialy containers
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
        )
    except:
        print("Timeout waiting for heading to load")
    #times out if no h1 headers are found

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    #parses the headers
    headings = soup.find_all(['h1', 'h2', 'h3'])
    print("Total headings found: ", len(headings))
    output += "Total headings found: " + str(len(headings)) +"\n\n"
    #cleans the headings
    for h in headings:
        text = re.sub(r'\s+', ' ', h.get_text()).strip()
        output = output+text+"\n"
    output = output+"\nEnd Scraping\n\n"
driver.quit()

#writes to file output string, which includes entirety of program
with open("urlOutput.txt", "w", encoding="utf-8") as f:
    f.write(output)
print("done")
