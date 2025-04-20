from playwright.sync_api import sync_playwright

BASE_URL = "https://www.sony.co.uk"
CATEGORY_URL = BASE_URL + "/store/search?query=:relevance:normalSearch:true:category:gwx-audio:category:gwx-headphones"


def get_product_urls_from_page(page, page_number):
    paginated_url = f"{CATEGORY_URL}&currentPage={page_number}" if page_number > 0 else CATEGORY_URL
    page.goto(paginated_url)

    try:
        page.wait_for_selector("a[href^='/store/product/']", timeout=8000)
    except:
        print(f"Page {page_number} did not contain products or failed to load.")
        return []

    anchors = page.query_selector_all("a[href^='/store/product/']")
    urls = []

    for a in anchors:
        href = a.get_attribute("href")
        if href and href.startswith("/store/product/"):
            full_url = BASE_URL + href
            urls.append(full_url)

    return urls


def get_all_product_urls():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()

        all_urls = set()
        page_number = 0

        while True:
            print(f"Scraping page {page_number}")
            urls = get_product_urls_from_page(page, page_number)
            if not urls:
                break

            print(f"Found {len(urls)} product links")
            all_urls.update(urls)
            page_number += 1

        browser.close()
        return list(all_urls)

def scrape_product_details(page, url):
    try:
        page.goto(url, timeout=20000)
        page.wait_for_load_state("networkidle")

        #product name
        name = page.locator("h1").first.inner_text().strip()

        #product price
        price_text = page.locator("div.price").first.inner_text().strip()
        price = None
        if "£" in price_text:
            price_text = price_text.replace("£", "").replace(",", "").strip()
            price = float(price_text)

        # MPN 
        mpn = ""
        possible_mpn_blocks = page.locator("p, div").all_inner_texts()
        for line in possible_mpn_blocks:
            if "MPN" in line.upper():
                mpn = line.split("MPN:")[-1].strip()
                break
        if not mpn:
            mpn_element = page.locator("p.cx-code")
            if mpn_element.count() > 0:
                mpn = mpn_element.first.inner_text().strip()

        return {
            "name": name,
            "price": price,
            "mpn": mpn,
            "url": url
        }

    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return None
    
