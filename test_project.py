# test_project.py

from scraper import Scraper
from sentiment import SentimentAnalyzer

# Mock URL for testing (you can use a simple website)
MOCK_URLS = ["https://example.com/"]

def test_scraper_initialization():
    scraper = Scraper(MOCK_URLS, max_headings=5)
    assert scraper.url_list == MOCK_URLS
    assert scraper.max_headings == 5

def test_sentiment_analyzer_positive():
    analyzer = SentimentAnalyzer()
    prompts = ["I love sunny days."]
    result = analyzer.analyze(prompts)
    assert "positive" in result.lower()
