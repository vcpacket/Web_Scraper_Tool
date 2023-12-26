#Web Scraper
#Author: VCPacket

import requests
from bs4 import BeautifulSoup
import logging
import time
from fake_useragent import UserAgent  # For random User-Agent generation
from pathlib import Path

class WebScraper:
    def __init__(self):
        self.setup_logger()

    def setup_logger(self):
        # Initialize logging configuration
        log_file = 'scraper_log.txt'
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Web scraper started.")

    def get_random_user_agent(self):
        # Generate a random User-Agent for each request
        ua = UserAgent()
        return ua.random

    def send_request(self, url):
        # Send HTTP request with a random User-Agent header
        headers = {'User-Agent': self.get_random_user_agent()}
        response = requests.get(url, headers=headers)
        return response

    def scrape_website(self, url, output_file):
        try:
            # Send a request to the specified URL
            response = self.send_request(url)

            if response.status_code == 200:
                # Parse HTML content of the page
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a')

                # Save extracted data to the output file
                with open(output_file, 'w', encoding='utf-8') as file:
                    for link in links:
                        file.write(link['href'] + '\n')

                logging.info(f"Data has been successfully saved to {output_file}")

            else:
                logging.error(f"Failed to retrieve the page. Status code: {response.status_code}")

        except Exception as e:
            logging.exception(f"An error occurred: {str(e)}")

    def run_scraper(self, user_url, output_file):
        try:
            # Strip leading and trailing whitespaces from user input
            user_url = user_url.strip()
            output_file = output_file.strip()

            # Ensure output directory exists
            Path(output_file).parent.mkdir(parents=True, exist_ok=True)

            # Scrape the specified website
            self.scrape_website(user_url, output_file)

        except KeyboardInterrupt:
            print("\nScraping interrupted by user.")
            logging.warning("Web scraper interrupted by user.")
        except Exception as e:
            logging.exception(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Instantiate the WebScraper class
    scraper = WebScraper()

    # Accept user input for the website URL and output file name
    user_url = input("Enter the URL of the website to scrape (e.g., https://www.example.com) : ")
    output_file = input("Enter the name of the output file (e.g., output.txt): ")

    # Run the web scraper
    scraper.run_scraper(user_url, output_file)
