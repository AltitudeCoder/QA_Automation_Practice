from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # needed for GitHub Actions
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")
    search_box = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("QA Automation with Selenium\n")

    results = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.yuRUbf > a"))
    )
    assert len(results) > 0
    print(f"✅ Found {len(results)} results for QA Automation search.")
