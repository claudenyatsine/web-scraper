# Python Web Scraper

## Overview
This project is a simple web scraper that fetches and parses HTML content from a specified URL. It extracts relevant information and saves it in a CSV file.

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd python-web-scraper
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then, install the required libraries using pip:
   ```
   pip install requests beautifulsoup4
   ```

## Dependencies
- requests
- beautifulsoup4

## Usage Guide
1. Open the `web_scraper.py` file and modify the URL in the `scrape_data` function to the target website you want to scrape.
2. Run the script:
   ```
   python web_scraper.py
   ```
3. After execution, the scraped data will be saved in `scraped_data.csv`. You can open this file to view the extracted information.