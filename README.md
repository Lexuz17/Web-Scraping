# Web-Scraping Collection

A collection of web scrapers for various platforms and purposes, built with Python.

## 🚀 Available Scrapers

### 1. Medium Scraper

Extract articles and engagement metrics from Medium.com

- Search-based article scraping
- Customizable article limit
- Extracts titles and clap counts
- CSV export functionality

```bash
# Run Medium scraper
cd medium-scrap
python medium.py
```

## 📋 Prerequisites

- Python 3.7+
- Chrome Browser
- ChromeDriver (matching your Chrome version)

## 🛠 Dependencies

```bash
pip install selenium
pip install beautifulsoup4
pip install lxml
```

## 🏗 Project Structure

```
Web-Scraping/
├── README.md
├── medium-scrap/
│   ├── medium.py
│   └── chromedriver-mac-arm64/
│       └── chromedriver
└── [future-scraper]/
    └── ...
```

## 🚦 Getting Started

1. Clone the repository:

   ```bash
   git clone [your-repo-url]
   cd Web-Scraping
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Setup ChromeDriver:

   - Download ChromeDriver matching your Chrome version
   - Place in appropriate scraper directory
   - Ensure executable permissions:
     ```bash
     chmod +x */chromedriver
     ```

4. Choose and run a scraper:
   ```bash
   cd [scraper-directory]
   python [scraper-name].py
   ```

## 📝 Usage Guidelines

### Medium Scraper

1. Enter your search query when prompted
2. Specify maximum number of articles (1-5000)
3. Wait for scraping to complete
4. Find results in `medium_articles.csv`

## 🔜 Upcoming Scrapers

- Twitter Data Scraper
- LinkedIn Company Scraper
- YouTube Comments Scraper
- Wikipedia Article Scraper

## 📚 Related Medium Article

Want to learn more about this project? Check out our detailed Medium article:

### [Everybody Can Scrape Right Now – Here's How!](your-medium-link)

Share your experience using this scraper by:

1. Clapping for the article
2. Commenting your use case
3. Sharing with your network
4. Contributing to the project

Join our community of data enthusiasts and help improve the project!
