from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import time
import csv
import os

def get_current_article_count(soup):
    return len(soup.find_all('article'))

def scrape_medium(search_query, target_articles=5000):
    # Setup Chrome driver
    service = Service('./chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service=service)
    
    formatted_query = search_query.replace(' ', '+')
    url = f'https://medium.com/search?q={formatted_query}'
    
    try:
        # Load the page
        driver.get(url)
        time.sleep(5)  # Initial wait for content to load
        
        clicks = 0
        consecutive_same_count = 0 
        previous_count = 0
        
        while True:
            soup = BeautifulSoup(driver.page_source, 'lxml')
            current_count = get_current_article_count(soup)
            
            print(f"Current articles found: {current_count}")
            
            # Check if we've reached our target
            if current_count >= target_articles:
                print(f"Reached target of {target_articles} articles!")
                break
                
            # Check if we're still getting new articles
            if current_count == previous_count:
                consecutive_same_count += 1
                if consecutive_same_count >= 3:  # If count hasn't changed in 3 attempts, assume no more articles
                    print("No more articles available to load")
                    break
            else:
                consecutive_same_count = 0
            
            try:
                # Wait for the "Show more" button to be clickable
                show_more = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ow.ox.ai.fa"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", show_more)
                time.sleep(2)
                show_more.click()
                time.sleep(3) 
                
                clicks += 1
                previous_count = current_count
                print(f"Clicked 'Show more' {clicks} times")
                
            except (TimeoutException, NoSuchElementException) as e:
                print("No more 'Show more' button found")
                break
        
        # Get final page source
        soup = BeautifulSoup(driver.page_source, 'lxml')
        articles = soup.find_all('article')
        
        # Prepare data for CSV
        articles_data = []
        
        for idx, article in enumerate(articles, 1):
            try:
                # Get title
                title = article.find('h2').text.strip()
                
                # Get claps count
                claps = '0'
                clap_div = article.find('div', class_='ac r nu')
                if clap_div:
                    clap_span = clap_div.find('span')   
                    if clap_span:
                        claps = clap_span.text.strip()
                
                articles_data.append({
                    'title': title,
                    'claps': claps
                })
                
                if idx % 100 == 0:
                    print(f"Processed {idx} articles...")
                
            except Exception as e:
                print(f"Error processing article: {e}")
                continue
        
        # Save to CSV
        csv_filename = 'medium_articles.csv'
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'claps']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(articles_data)
            
        print(f"Found total of {len(articles_data)} articles")
        print(f"Data has been saved to {csv_filename}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    print("\n=== Medium Article Scraper ===")
    search_query = input("Enter your Medium search query: ")
    max_articles = int(input("Enter maximum number of articles to scrape: "))
    print(f"\nStarting scraping for '{search_query}' with max {max_articles} articles...")
    scrape_medium(search_query, max_articles)
