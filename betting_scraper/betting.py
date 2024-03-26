from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import os
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

os.environ['PATH'] += r"C:/Users/white/Documents/Web Scraping Files/SeleniumDriver"
driver.get('https://www.adamchoi.co.uk/overs/detailed') 

#wait = WebDriverWait(driver, 10)
#all_matches_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@analytics-event = 'All matches']")))
#all_matches_button.click()

all_matches_button = driver.find_element(By.XPATH, "//label[@analytics-event = 'All matches']")
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, "tr")

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, "./td[1]").text)
    home_team.append(match.find_element(By.XPATH, "./td[2]").text)
    score.append(match.find_element(By.XPATH, "./td[3]").text)
    away_team.append(match.find_element(By.XPATH, "./td[4]").text)

driver.quit()

df = pd.DataFrame({'date': date, 'home_team': home_team,'score': score,'away_team': away_team})
df.to_csv('data.csv', index=False)
print(df)
