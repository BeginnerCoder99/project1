# p2.py Website Headline Scraper
The program will read from a url_list.txt file the first three urls. It will then scrape all h1, h2, and h3 files. Then it will put them all in a urlOutput.txt file, creating it if necessary. We use Selenium with headless browser to do website emulation and BeautifulSoup & lxml to parse everything

## Installation
pip install requests, beautifulsoup4, lxml, selenium, and webdriver-manager

## How to Use
Create a url_list.txt file with exactly 3 urls. Make sure it is inside the same directory as p2.py. Once that is done, simply run the p2.py program. After running the program, the results should be saved to urlOutput.txt.

## Notes
It uses headless chrome to emulate the program. If a url has good bot protection, the program will not work. You might need to search for urls that are friendly to scraping or do not have good anti-bot security. If the website doesn't have an h1 header, it will timeout after 30 seconds. I used UTF-8 to handle unicode since it was throwing exceptions when writing to a txt file.

