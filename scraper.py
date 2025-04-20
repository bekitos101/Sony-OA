
from scraper_utils import get_all_product_urls, scrape_product_details
from playwright.sync_api import sync_playwright
import csv

if __name__ == "__main__":
    all_product_urls = get_all_product_urls()
    print(f"\n Total unique products: {len(all_product_urls)}\n")

    scraped_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()

        for idx, url in enumerate(all_product_urls):
            print(f"🔎 [{idx+1}/{len(all_product_urls)}] Scraping: {url}")
            details = scrape_product_details(page, url)
            if details:
                print(f"✔ Scraped: {details['name']}")
                scraped_data.append(details)
            else:
                print("An error occured")

        browser.close()

    with open("headphones_data.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price", "mpn", "url"])
        writer.writeheader()
        writer.writerows(scraped_data)

    print(f"\n Exported {len(scraped_data)} products to headphones_data.csv")
    


    