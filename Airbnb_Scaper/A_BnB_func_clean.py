import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Configure Chrome WebDriver path
os.environ['PATH'] += r"C:\Users"
driver = webdriver.Chrome()

# Initialize browser and navigate to Airbnb
driver.get("https://www.airbnb.com/")
driver.maximize_window()
time.sleep(5)
wait = WebDriverWait(driver, 10)


def search(location, start, end, num_adults, num_beds):
    """
    Search for Airbnb listings with specified parameters.
    
    Args:
        location (str): Location to search for
        start (str): Check-in date
        end (str): Check-out date
        num_adults (int): Number of adults
        num_beds (int): Number of beds required
    """
    # Handle popup dismissal
    try:
        pop_up = wait.until(EC.element_to_be_clickable((
            By.XPATH, 
            '//*[@class="l1ovpqvx atm_1he2i46_1k8pnbi_10saat9 atm_yxpdqi_1pv6nv4_10saat9 atm_1a0hdzc_w1h1e8_10saat9 atm_2bu6ew_929bqk_10saat9 atm_12oyo1u_73u7pn_10saat9 atm_fiaz40_1etamxe_10saat9 c1h5tsj6 atm_1s_glywfm atm_5j_1ssbidh atm_9j_tlke0l atm_tl_1gw4zv3 atm_9s_1o8liyq atm_mk_h2mmj6 atm_l8_idpfg4 atm_gi_idpfg4 atm_3f_glywfm atm_26_1j28jx2 atm_7l_hkljqm atm_uc_10d7vwn atm_kd_glywfm atm_kd_glywfm_1w3cfyq atm_3f_glywfm_e4a3ld atm_l8_idpfg4_e4a3ld atm_gi_idpfg4_e4a3ld atm_3f_glywfm_1r4qscq atm_kd_glywfm_6y7yyg atm_kd_glywfm_pfnrn2_1oszvuo atm_l8_idpfg4_1icshfk_1oszvuo atm_gi_idpfg4_1icshfk_1oszvuo atm_3f_glywfm_b5gff8_1oszvuo atm_kd_glywfm_2by9w9_1oszvuo atm_k4_1piyxwk_1o5j5ji atm_9j_13gfvf7_1o5j5ji atm_uc_glywfm__1rrf6b5 atm_7l_wbi19n_1nos8r_uv4tnr atm_26_zbnr2t_1rqz0hn_uv4tnr atm_7l_1wxwdr3_4fughm_uv4tnr atm_26_1j28jx2_1r92pmq_uv4tnr atm_7l_wbi19n_csw3t1 atm_tr_ffmgpj_csw3t1 atm_26_zbnr2t_1ul2smo atm_3f_glywfm_jo46a5 atm_l8_idpfg4_jo46a5 atm_gi_idpfg4_jo46a5 atm_3f_glywfm_1icshfk atm_kd_glywfm_19774hq atm_uc_aaiy6o_1w3cfyq atm_70_glywfm_1w3cfyq atm_uc_glywfm_1w3cfyq_1rrf6b5 atm_70_1e7pbig_9xuho3 atm_26_zbnr2t_9xuho3 atm_uc_aaiy6o_pfnrn2_1oszvuo atm_70_glywfm_pfnrn2_1oszvuo atm_uc_glywfm_pfnrn2_1o31aam atm_70_1e7pbig_1buez3b_1oszvuo atm_26_zbnr2t_1buez3b_1oszvuo atm_7l_1wxwdr3_1o5j5ji atm_26_1j28jx2_154oz7f atm_92_1yyfdc7_vmtskl atm_9s_1ulexfb_vmtskl atm_mk_stnw88_vmtskl atm_tk_1ssbidh_vmtskl atm_fq_1ssbidh_vmtskl atm_tr_pryxvc_vmtskl atm_5j_1ssbidh_vmtskl atm_vy_1vi7ecw_vmtskl atm_e2_1vi7ecw_vmtskl dir dir-ltr"]'
        )))
        pop_up.click()
    except:
        print('No popup to dismiss')
    
    # Basic search form navigation
    place = wait.until(EC.element_to_be_clickable((By.ID, 'bigsearch-query-location-input')))
    place.click()
    
    date_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Check in')]")))
    date_out = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Check out')]")))
    
    # Enter location
    place.send_keys(location)
    time.sleep(1)
    
    # Select check-in date yyyy-mm-dd
    date_in.click()
    start_selector = f'button[data-state--date-string="{start}"]'
    start_day = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, start_selector)))
    start_day.click()
    
    # Select check-out date yyyy-mm-dd
    date_out.click()
    date_out.click()
    end_selector = f'button[data-state--date-string="{end}"]'
    end_day = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, end_selector)))
    end_day.click()
    date_out.click()
    
    # Add guests
    people = wait.until(EC.element_to_be_clickable((
        By.XPATH, 
        '//*[@class="fbb0tkq atm_c8_86zae atm_g3_1s00pb0 atm_fr_1h5ikn atm_cs_6adqpa atm_7l_1esdqks atm_vv_1q9ccgz atm_ks_zryt35 atm_sq_1l2sidv dir dir-ltr"]'
    )))
    people.click()
    
    add_peeps = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 
        '.piqlc25 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(3)'
    )))
    
    # Add specified number of adults
    x = 0
    while x < num_adults:    
        add_peeps.click()
        time.sleep(.7)
        x += 1
    
    # Perform search
    go = wait.until(EC.element_to_be_clickable((
        By.XPATH, 
        '//*[@class="s15knsuf atm_c8_1nkr7pq atm_g3_1e1y0tv atm_fr_yucz6i atm_cs_10d11i2 atm_li_1y44olf dir dir-ltr"]'
    )))
    go.click()

    # Apply bed filter
    filter_open = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cvirtb6')))
    filter_open.click()
    
    beds = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 
        '#stepper-filter-item-min_beds-stepper > button:nth-child(3)'
    )))
    
    # Set minimum number of beds
    y = 0
    while y < num_beds:
        beds.click()
        time.sleep(.7)
        y += 1
        
    go2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.p13966et')))
    go2.click()
    time.sleep(3)


def scrape(file_name_to_save):
    """
    Scrape Airbnb listings from search results and save to CSV.
    
    Args:
        file_name_to_save (str): Name of the CSV file to save results
    """
    data = []
    n = 0
    
    # Continue scraping until no more pages
    while n != 1:
        time.sleep(2)
        appart_pods = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.gsgwcjk > div')))
        
        for i in appart_pods:
            class_attr = i.get_attribute("class")
            if '' == class_attr:
                listing = {}
                
                # Extract title
                try:
                    listing["title"] = i.find_element(By.CSS_SELECTOR, 'meta[itemprop="name"]').get_attribute('content')
                except NoSuchElementException:
                    listing["title"] = None
                
                # Extract type
                try: 
                    listing["type"] = i.find_element(By.CSS_SELECTOR, "div[data-testid='listing-card-title']").text.strip()
                except NoSuchElementException:
                    listing["type"] = None
                
                # Extract price
                try:
                    listing["price"] = i.find_element(By.CSS_SELECTOR, "div[data-testid='price-availability-row'] div[role ='presentation'] > div > div > span > div:nth-child(1) > span").text.strip()
                except NoSuchElementException:
                    listing["price"] = None
                
                # Extract reviews
                try:
                    listing['reviews'] = i.find_element(By.CSS_SELECTOR, "div[data-testid='card-container'] > div > div:nth-child(2) > div:nth-child(7) > span > span:nth-child(3)").text.strip()
                except NoSuchElementException:
                    listing['reviews'] = None
                
                # Extract link
                try:
                    listing["link"] = i.find_element(By.CSS_SELECTOR, 'div[itemprop="itemListElement"] > div > div > div > a').get_attribute('href')
                except NoSuchElementException:
                    listing["link"] = None
                
                # Only add to data if we found at least some information
                if listing and any(listing.values()):
                    data.append(listing)

        # Handle pagination
        try:
            next_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cn6uggc [aria-label="Next"]')))
            next_btn.click()
        except TimeoutException:
            n = 1
            # Create DataFrame and display results
            df = pd.DataFrame(data)
            print(df.head())

            # Save to CSV
            if not df.empty:
                df.to_csv(file_name_to_save, index=False)
                print("Data saved to " + file_name_to_save)
            else:
                print("No data found to save")
    