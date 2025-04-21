# Sony Headphones Web Scraper

This Python project scrapes product data for headphones from [sony.co.uk](https://www.sony.co.uk).  
It extracts:

-  Product Name  
-  Current Price  
-  MPN (Manufacturer Part Number)  
-  Product Page URL  

##  Approach

I used **Playwright** for fast browser automation. The scraper performs the following steps:

1. **Gathers all product URLs** using dynamic pagination to ensure it scales with newly added products.
2. **Extracts relevant data** (name, price, MPN, URL) from each product page using flexible CSS selectors and including fallback handling for inconsistencies in how it's displayed.
3. **Exports the final results to a CSV file**


##  Requirements

- **Python 3.12+**  

- **Git Bash** (for Windows) or **any Unix-compatible shell** (Linux/macOS)  
  Required to run the Bash script for setup and execution.

## How to Run

Just run the Bash script:
```bash
./run_scraper.sh 


