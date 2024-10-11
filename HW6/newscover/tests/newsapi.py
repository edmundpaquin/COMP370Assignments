import unittest
import json
from newscover.newsapi import fetch_latest_news
from datetime import datetime, timedelta

class TestFetchLatestNews(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load API key from test_secrets.json
        with open('newscover/tests/test_secrets.json') as f:
            secrets = json.load(f)
        cls.api_key = secrets['api_key']

    def test_no_keywords_provided(self):
        # Test that the function raises a ValueError if no keywords are provided
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key=self.api_key, news_keywords=[])

    def test_lookback_days_limit(self):
    # Test that articles returned are within the specified lookback_days timeframe
        articles = fetch_latest_news(api_key=self.api_key, news_keywords=['technology'], lookback_days=7)
        
        today = datetime.now()  # Use UTC to match NewsAPI's response
        lookback_date = today - timedelta(days=7)

        for article in articles:
            published_at = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            # Ensure published_at is within the lookback period
            self.assertGreaterEqual(published_at.day, lookback_date.day)

    def test_invalid_keyword(self):
        # Test that the function raises a ValueError if a keyword contains non-alphabetic characters
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key=self.api_key, news_keywords=['tech1!23'])

if __name__ == '__main__':
    unittest.main()