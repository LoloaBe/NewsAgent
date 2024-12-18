# NewsAgent

## Overview
NewsAgent is a Python application that fetches, deduplicates, and summarizes news articles for selected topics. The news feed can be saved to a file and displayed in the terminal.

## Features
- Fetches news articles from multiple RSS feeds (Technology, Finance, Local, German, Italian).
- Deduplicates news articles across multiple categories.
- Displays a personalized news report based on user preferences.
- Saves the news report to a text file.

## Installation
### Prerequisites
- Python 3.10 or higher
- Virtual Environment (optional but recommended)

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd NewsAgent
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the program using the following command:
```bash
python main.py
```

### Output
- The personalized news report will be displayed in the terminal.
- The report will also be saved as `personalized_news_report.txt` in the project directory.

## File Structure
```
NewsAgent/
├── main.py                 # Entry point of the application
├── news_agent.py           # Core logic for fetching and generating reports
├── news_aggregator.py      # Aggregates and deduplicates news articles
├── requirements.txt        # Project dependencies
├── personalized_news_report.txt  # Generated news report
├── .gitignore              # Ignore unnecessary files
└── README.md               # Project documentation
```

## Dependencies
- `requests` - HTTP requests to fetch RSS feeds.
- `beautifulsoup4` - Parsing XML and HTML content.
- `hashlib` - Deduplication of articles using hash.

## Author
Your Name - [Your Contact Info]

## License
This project is licensed under the MIT License.

## Contributing
Feel free to open issues or submit pull requests to improve the project.
