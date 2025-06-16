import requests
from playwright.sync_api import sync_playwright
import time

class Scraper:
    def __init__(self):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch_persistent_context(user_data_dir="./linkedin_profile", headless=False)
        self.page = self.browser.new_page()
        self.logged_in = False

    def login(self):
        if not self.logged_in:
            self.page.goto("https://www.linkedin.com/login")
            self.logged_in = True

    def scrape_postings(self, query, max_results=50):
        self.login()
        search_url = f"https://www.linkedin.com/jobs/search/?keywords={query.replace(' ', '%20')}"
        self.page.goto(search_url)

        jobs = []

        for _ in range(1, 6):
            self.page.wait_for_selector('div.job-card-container')

            job_cards = self.page.query_selector_all('div.job-card-container')
            print(f"Found {len(job_cards)} job cards.")

            for card in job_cards:
                try:
                    title = card.query_selector('a.job-card-container__link').inner_text().strip()
                    company = card.query_selector('div.artdeco-entity-lockup__subtitle').inner_text().strip()
                    link = card.query_selector('a.job-card-container__link').get_attribute('href')
                    full_link = f"https://www.linkedin.com{link}"

                    job = {
                        'title': title,
                        'company': company,
                        'link': full_link
                    }
                    print(job)
                    jobs.append(job)
                except Exception as e:
                    print(f"Error parsing card: {e}")
            index = _ * 25
            search_url = search_url + f"&start={index}"
            self.page.goto(search_url)
        return jobs

