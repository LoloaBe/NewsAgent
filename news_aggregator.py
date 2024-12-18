import hashlib
import os
import requests
from bs4 import BeautifulSoup

class NewsAggregator:
    def __init__(self):
        """
        Initialize the NewsAggregator class.
        Add any configurations or API setup required.
        """
        self.sources = {
            "Technology": "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
            "Finance": "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
            "Local": "https://rss.nytimes.com/services/xml/rss/nyt/NYRegion.xml",
            "German": "https://rss.sueddeutsche.de/rss/Topthemen",
            "Italian": "https://www.ilsole24ore.com/rss/primapagina.xml"
        }

    def get_articles_by_topic(self, topic):
        """
        Fetch articles for a given topic using an RSS feed or web scraping.
        :param topic: Topic string to fetch articles for.
        :return: List of dictionaries with article title, summary, and link.
        """
        if topic not in self.sources:
            print(f"No source configured for topic: {topic}")
            return []

        url = self.sources[topic]
        try:
            print(f"Fetching articles from {url} for topic: {topic}")
            response = requests.get(url)
            response.raise_for_status()

            # Example: Parse RSS feed
            soup = BeautifulSoup(response.content, 'xml')
            articles = []
            for item in soup.find_all('item'):
                title = item.title.text
                link = item.link.text
                summary = item.description.text if item.description else "No summary available"
                articles.append({"title": title, "summary": summary, "link": link})

            return articles
        except Exception as e:
            print(f"Error fetching articles for topic {topic}: {e}")
            return []

    def deduplicate(self, agents):
        """
        Deduplicate articles across multiple agents by hashing titles.
        :param agents: List of NewsAgent instances.
        """
        seen_hashes = set()
        for agent in agents:
            deduplicated = []
            for article in agent.articles:
                article_hash = hashlib.md5(article['title'].encode('utf-8')).hexdigest()
                if article_hash not in seen_hashes:
                    seen_hashes.add(article_hash)
                    deduplicated.append(article)
            agent.articles = deduplicated

    def get_combined_news(self, agents):
        """
        Combine articles from multiple agents into a single list.
        :param agents: List of NewsAgent instances.
        :return: Combined list of articles.
        """
        combined = []
        for agent in agents:
            combined.extend(agent.articles)

        # Print results to terminal
        print("\n### Combined News Feed ###\n")
        for idx, article in enumerate(combined, start=1):
            print(f"{idx}. Title: {article['title']}")
            print(f"   Summary: {article['summary']}")
            print(f"   Link: {article['link']}\n")

        return combined
