from playwright.sync_api import sync_playwright

def dump_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto(url, timeout=20000)
        page.wait_for_load_state("networkidle")

        html = page.content()
        filename = url.split("/")[-2] + ".html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"Dumped HTML to {filename}")
        browser.close()

if __name__ == "__main__":
    test_url = "https://www.sony.co.uk/store/product/wh1000xm5p.ce7/WH-1000XM5-Wireless-Noise-Cancelling-Headphones"
    dump_html(test_url)
