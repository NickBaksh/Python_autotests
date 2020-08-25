from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_yandex_search():
    driver = WebDriver(executable_path='C://Chrome driver 84//chromedriver.exe')
    driver.get('http://www.ya.ru')
    search_input = driver.find_element_by_xpath('//input[@id="text"]')
    search_button = driver.find_element_by_xpath('//div[@class="search2__button"]//button[@type="submit"]')
    search_input.send_keys('market.yandex.ru')
    search_button.click()

    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="organic__url-text"]')))
    search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
    link = search_results[0].find_element_by_xpath('.//h2/a')
    link.click()
    driver.switch_to.window(driver.window_handles[1])