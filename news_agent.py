import os

# Attempt to import NewsAggregator. Handle import errors gracefully.
try:
    from news_aggregator import NewsAggregator
except ModuleNotFoundError as e:
    raise ImportError("The module 'news_aggregator' could not be found. Ensure it exists and is in the correct directory.") from e

class NewsAgent:
    def __init__(self):
        self.aggregator = NewsAggregator()
        self.agents = [
            {"name": "tech_agent", "topic": "Technology"},
            {"name": "finance_agent", "topic": "Finance"},
            {"name": "local_agent", "topic": "Local"},
            {"name": "german_agent", "topic": "German"},
            {"name": "italian_agent", "topic": "Italian"}
        ]

    def fetch_articles(self, topic):
        """
        Fetch articles for a specific topic using NewsAggregator.
        Ensures at least three articles are returned.
        """
        print(f"Fetching articles for topic: {topic}")
        articles = self.aggregator.get_articles_by_topic(topic)
        if len(articles) < 3:
            print(f"Warning: Fewer than 3 articles found for {topic}. Fetching additional placeholder articles.")
            # Add placeholder articles to ensure at least 3 entries
            while len(articles) < 3:
                articles.append({
                    "title": f"Placeholder article for {topic}",
                    "link": "#"
                })
        return articles[:3]  # Ensure exactly 3 articles

    def generate_report(self):
        """
        Generate a personalized news report for all agents.
        """
        report = "### Personalized News Report ###\n\n"
        for agent in self.agents:
            name, topic = agent["name"], agent["topic"]
            articles = self.fetch_articles(topic)
            report += f"--- {name} ---\n"
            for idx, article in enumerate(articles, start=1):
                report += f"{idx}. {article['title']} - {article['link']}\n"
            report += "\n"
        return report

    def save_report(self, report, file_path="personalized_news_report.txt"):
        """
        Save the generated report to a file.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(report)
        print(f"Report saved to {file_path}.")

if __name__ == "__main__":
    try:
        agent = NewsAgent()
        news_report = agent.generate_report()
        agent.save_report(news_report)
    except ImportError as e:
        print(e)
