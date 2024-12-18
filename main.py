from news_agent import NewsAgent

def main():
    """
    Main entry point for generating, saving, and displaying the news report.
    """
    print("Starting NewsAgent...")
    agent = NewsAgent()
    report = agent.generate_report()
    
    # Print the report to the terminal
    print("\n### Personalized News Report ###\n")
    print(report)
    
    # Save the report to a file
    agent.save_report(report)
    print("News report generation complete.")

if __name__ == "__main__":
    main()
