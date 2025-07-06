import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException

os.environ['PATH'] += r"C:\Users\sowen\OneDrive\Documents\Python\Selenium\Setup"
driver = webdriver.Chrome()

# Alternative: Use ChromeDriverManager for automatic driver management
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

actions = ActionChains(driver)

try:
    driver.get("https://www.chicagomusicexchange.com/collections/electric-guitars")
    driver.maximize_window()
    
    # Use explicit wait instead of implicit wait for better control
    wait = WebDriverWait(driver, 10)
    
    # Handle popup with explicit wait and proper exception handling
    try:
        escape = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#ltkpopup-close-button > a')))
        escape.click()
        time.sleep(1)  # Brief pause after closing popup
    except TimeoutException:
        print("No popup found or popup didn't appear within timeout")
    
    # Uncomment and fix these if you need to navigate through menus
    # hover_menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.gm-level-0:nth-child(1) > a:nth-child(1)")))
    # hover_menu.click()
    # eguit_filt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.gm-level-0:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > ul:nth-child(1) > li:nth-child(10) > a:nth-child(1) > span:nth-child(1)")))
    # eguit_filt.click()
    
    data = []
    
    # Load more products if needed
    for x in range(5):
        try:
            load_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.collection-load-more")))
            load_button.click()
            time.sleep(2)  # Wait for content to load
        except TimeoutException:
            print("No more 'Load More' button found")
            break
    
    # Wait for products to load
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul#product-grid > li")))
    
    pods = driver.find_elements(By.CSS_SELECTOR, "ul#product-grid > li")
    print(f"Found {len(pods)} products")
    
    for i, pod in enumerate(pods):
        guitar = {}
        
        # Use more specific exception handling
        try:
            guitar["listing"] = pod.find_element(By.CSS_SELECTOR, "div.product-card-header > h3").text.strip()
        except NoSuchElementException:
            guitar["listing"] = None
        
        try:
            guitar["price"] = pod.find_element(By.CSS_SELECTOR, "div.price__container > div > span:nth-child(2)").text.strip()
        except NoSuchElementException:
            guitar["price"] = None
        
        try:
            guitar["serial"] = pod.find_element(By.CSS_SELECTOR, "span.ss__info__badge--serial").text.strip()
        except NoSuchElementException:
            guitar["serial"] = None
        
        try:
            guitar["condition"] = pod.find_element(By.CSS_SELECTOR, "li.product-badge").text.strip()
        except NoSuchElementException:
            guitar["condition"] = None
        
        try:
            guitar["weight"] = pod.find_element(By.CSS_SELECTOR, "span.ss__info__badge--weight").text.strip()
        except NoSuchElementException:
            guitar["weight"] = None
        
        try:
            guitar["stock"] = pod.find_element(By.CSS_SELECTOR, "span.product-card-inventory__stock").text.strip()
        except NoSuchElementException:
            guitar["stock"] = None
        
        # Only add to data if we found at least some information
        if any(guitar.values()):
            data.append(guitar)
            print(f"Processed product {i+1}: {guitar.get('listing', 'Unknown')}")
    
    # Create DataFrame and display results
    df = pd.DataFrame(data)
    print(f"\nScraped {len(df)} products successfully")
    print(df.head())
    
    # Save to CSV
    if not df.empty:
        df.to_csv("guitar_products.csv", index=False)
        print("Data saved to guitar_products.csv")
    else:
        print("No data found to save")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Always close the driver
    driver.quit()