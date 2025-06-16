from src.linkedin_scraper import Scraper
from src.text_utils import save_to_csv

# add more keywords as needed
scraper = Scraper()
queries = ["embedded systems", "robotics"]
scraped_jobs = []

for q in queries:
    result = scraper.scrape_postings(q)
    scraped_jobs.append(result)

save_to_csv(scraped_jobs)

print(f"\nScraped for {len(scraped_jobs)} queries!")