import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Setup logging
logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def scrape_jobs_from_file(html_file, output_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    jobs = []
    # Find all job cards
    job_cards = soup.find_all('a', class_='job-listing with-apply-button')[:10]
    print(f"Found {len(job_cards)} job cards.")

    for card in job_cards:
        try:
            # Job Title
            title_tag = card.find('h3', class_='job-listing-title')
            title = title_tag.get_text(strip=True) if title_tag else "N/A"

            # Company
            company = "N/A"
            company_li = card.find('i', class_='icon-material-outline-business')
            if company_li and company_li.parent:
                company = company_li.parent.get_text(strip=True).replace('', '').strip()

            # Location
            location = "N/A"
            location_li = card.find('i', class_='icon-material-outline-location-on')
            if location_li and location_li.parent:
                location = location_li.parent.get_text(strip=True).replace('', '').strip()

            # Expiry Date
            expiry = "N/A"
            expiry_li = card.find('i', class_='icon-material-outline-access-time')
            if expiry_li and expiry_li.parent:
                expiry = expiry_li.parent.get_text(strip=True).replace('', '').replace('Expires:', '').strip()

            # Job Description (not available in the listing, would need to follow the link)
            job_desc = "N/A"

            jobs.append({
                'Job Title': title,
                'Company': company,
                'Location': location,
                'Expiry Date': expiry,
                'Job Description': job_desc
            })
        except Exception as e:
            logging.warning(f"Error parsing job card: {e}")
            continue

    df = pd.DataFrame(jobs).drop_duplicates()
    df.to_csv(output_file, index=False, encoding='utf-8')
    logging.info(f"Scraped {len(df)} jobs to {output_file}")
    print(f"Scraped {len(df)} jobs to {output_file}")

if __name__ == "__main__":
    html_file = 'vacancymail_jobs.html.html'  # Use the actual file name
    output_file = 'scraped_data.csv'
    scrape_jobs_from_file(html_file, output_file)