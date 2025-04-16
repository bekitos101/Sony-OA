from playwright.sync_api import sync_playwright

def extract_product_urls():
    base_url = "https://www.sony.co.uk/store/search?query=:relevance:normalSearch:true:category:gwx-audio:category:gwx-headphones"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        page = browser.new_page()
        page.goto(base_url)

        # Wait for at least one product tile by text
        page.wait_for_selector("text=Headphones", timeout=10000)

        print("Page loaded:", page.title())

        # Try to find anchors inside rendered product cards
        anchors = page.query_selector_all("a[href^='/store/product/']")
        print(f"Found {len(anchors)} product links")

        product_urls = []
        for a in anchors:
            href = a.get_attribute("href")
            if href:
                full_url = "https://www.sony.co.uk" + href
                print("Found product:", full_url)
                product_urls.append(full_url)

        browser.close()
        return product_urls

if __name__ == "__main__":
    urls = extract_product_urls()
    print("\nExtracted URLs:")
    for url in urls:
        print(url)
