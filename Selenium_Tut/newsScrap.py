import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Reconfigure stdout to handle utf-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Initialize the WebDriver (Chrome)
driver = webdriver.Chrome()

# List to store all the scraped headlines
headlines = []

# Number of pages to scrape
num_pages = 1

# Start the loop for scraping multiple pages
for i in range(0, num_pages * 10, 10):  # `i` will be 0, 10, 20, ..., 990
    driver.get(f"https://www.google.com/search?q=apple+stock+price&sca_esv=28194934ae825b70&sca_upv=1&rlz=1C1VDKB_en-GBIN1079IN1079&tbm=nws&ei=E0zJZpm8O8SG4-EP3fHfgQE&start={i}&sa=N&ved=2ahUKEwjZke_o0IyIAxVEwzgGHd34NxA4ChDy0wN6BAgCEAc&biw=1536&bih=776&dpr=1.25")

    try:
        # Wait for headlines to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "n0jPhd"))
        )

        # Find all elements containing headlines
        elems = driver.find_elements(By.CLASS_NAME, "n0jPhd")

        print(f"{len(elems)} headlines found on page {i//10 + 1}")

        # Append each headline to the list
        for elem in elems:
            headline = elem.text
            headlines.append(headline)  # Append headline to the list
            print(f"Appended headline: {headline}")

    except Exception as e:
        print(f"An error occurred on page {i//10 + 1}: {e}")

    # Optional delay to avoid bot detection
    time.sleep(4)

# Close the WebDriver
driver.close()

# Optionally, print the collected headlines
for idx, headline in enumerate(headlines, start=1):
    print(f"{idx}: {headline}")

# If needed, you can save the headlines to a file later
output_file = "newsData/apple_headlines.txt"
os.makedirs("newsData", exist_ok=True)

with open(output_file, 'w', encoding="utf-8") as f_out:
    for headline in headlines:
        f_out.write(headline + "\n")

print(headlines)