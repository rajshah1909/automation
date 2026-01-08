from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv
import re

CHROMEDRIVER_PATH = r"C:\chromedriver-win64\chromedriver.exe"
options = Options()
# options.add_argument("--headless")
service = Service(CHROMEDRIVER_PATH)

CITY_URLS = [
    "https://www.deltadental.com/us/en/member/find-a-dentist/delaware/dover-dentists.html",
    "https://www.deltadental.com/us/en/member/find-a-dentist/delaware/wilmington-dentists.html",
    "https://www.deltadental.com/us/en/member/find-a-dentist/delaware/newark-dentists.html",
    "https://www.deltadental.com/us/en/member/find-a-dentist/delaware/middletown-dentists.html",
    "https://www.deltadental.com/us/en/member/find-a-dentist/delaware/glasgow-dentists.html"
    ]

def proper_case(s):

    return s.title() if s else ""

def get_city_name(url):
    match = re.search(r'/find-a-dentist/delaware/([^-]+(?:-[^-]+)*)-dentists\.html', url)
    if match:
        city = match.group(1).replace('-', ' ')
        return proper_case(city)
    return ""

def extract_dentists(driver, city, seen_emails):
    dentists = []
    cards = driver.find_elements(By.CSS_SELECTOR, "div.dentist-result.result-visible")
    for card in cards:
        try:
            first_name = card.find_element(By.CSS_SELECTOR, "span.first-name").text.strip()
            first_name = proper_case(first_name)
        except:
            first_name = ""
        try:
            last_name = card.find_element(By.CSS_SELECTOR, "span.last-name").text.strip()
            last_name = proper_case(last_name)
        except:
            last_name = ""
        # Practice Name
        practice_name = ""
        try:
            practice_elems = card.find_elements(By.CSS_SELECTOR, "p.info-detail.dentist-office")
            for elem in practice_elems:
                txt = elem.text.strip()
                if txt:
                    practice_name = proper_case(txt)
                    break
        except:
            pass
        # Expand details
        try:
            view_more = card.find_element(By.CSS_SELECTOR, ".dentist-other-info-title")
            driver.execute_script("arguments[0].click();", view_more)
            time.sleep(1)
        except:
            pass
        # Email
        try:
            email_elem = card.find_element(By.CSS_SELECTOR, ".dentist-other-info .dentist-email .info-detail a")
            email = email_elem.text.strip().lower()
        except:
            email = ""
        # Only add if email is not empty and not already seen
        if email and email not in seen_emails:
            dentists.append([first_name, last_name, practice_name, email, city])
            seen_emails.add(email)
    return dentists

all_dentists = []
seen_emails = set()

driver = webdriver.Chrome(service=service, options=options)
for url in CITY_URLS:
    city = get_city_name(url)
    print(f"Scraping dentists for {city} ...")
    driver.get(url)
    time.sleep(5)
    # Go through all pages for each city
    for page in range(1, 8):
        all_dentists.extend(extract_dentists(driver, city, seen_emails))
        # Next page logic
        if page < 7:
            try:
                next_btn = driver.find_element(By.CSS_SELECTOR, "li.next a")
                driver.execute_script("arguments[0].click();", next_btn)
                time.sleep(5)
            except Exception as e:
                print(f"Could not go to page {page+1} for {city}: {e}")
                break
driver.quit()

with open("city.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["First Name", "Last Name", "Practice Name", "Email Address", "City"])
    writer.writerows(all_dentists)

print(f"Saved {len(all_dentists)} dentists to city.csv")