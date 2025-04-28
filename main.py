# main.py

from scraper import Scraper
from sentiment import SentimentAnalyzer

def read_url_list(filename):
    with open(filename) as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls

def read_scraped_text(filename):
    with open(filename, encoding="utf-8") as file:
        prompts = [line.strip() for line in file if line.strip()]
    return prompts

def main():
    url_list = read_url_list("url_list.txt")
    
    # Scrape headings
    scraper = Scraper(url_list, max_headings=20)
    scraped_output = scraper.run()
    scraper.save_output("urlOutput.txt", scraped_output)
    scraper.quit()

    # Sentiment analysis
    prompts = read_scraped_text("urlOutput.txt")
    analyzer = SentimentAnalyzer()
    ai_response = analyzer.run(prompts)

    # Save AI output
    with open("AIoutput.txt", "w", encoding="utf-8") as f:
        f.write(ai_response)

    print("Done")

if __name__ == "__main__":
    main()
