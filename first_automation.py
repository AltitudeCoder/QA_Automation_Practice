# first_automation.py
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Launch Chrome using undetected-chromedriver
driver = uc.Chrome()

try:
    # Step 2: Open Google
    driver.get("https://www.google.com")

    # Step 3: Wait for search bar to appear
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Step 4: Enter search query and press Enter
    search_box.send_keys("QA automation")
    search_box.send_keys(Keys.RETURN)

    # Step 5: Wait for search results to load
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='g']//h3/ancestor::a")
        )
    )

    # Step 6: Print the first 5 results (title + URL)
    for index, result in enumerate(results[:5], start=1):
        title = result.find_element(By.TAG_NAME, "h3").text
        url = result.get_attribute("href")
        print(f"{index}. {title} -> {url}")

finally:
    # Step 7: Close the browser
    driver.quit()
