from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import allure
from allure import severity, severity_level


@allure.title('Количество результатов поиска больше 10')
@severity(severity_level.CRITICAL)
def test_yandex_search():
    driver = WebDriver(executable_path='C://Chrome driver 84//chromedriver.exe')
    with allure.step('Открываем страницу поиска'):
        driver.get('http://www.ya.ru')

    with allure.step('Открываем страницу market.yandex'):
        search_input = driver.find_element_by_xpath('//input[@id="text"]')
        search_button = driver.find_element_by_xpath('//div[@class="search2__button"]//button[@type="submit"]')
        search_input.send_keys('market.yandex.ru')
        search_button.click()

    def check_results_count(driver):
        inner_search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        return len(inner_search_results) >= 10

    with allure.step('Проверяем количество результатов поиска'):
        WebDriverWait(driver, 5, 0.5).until(check_results_count, 'The count less than 10')

    with allure.step('По первому результату переходим на страницу market.yandex'):
        search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        link = search_results[0].find_element_by_xpath('.//h2/a')
        link.click()

    driver.switch_to.window(driver.window_handles[1])
    with allure.step('Проверяем Title на корректность'):
        assert driver.title == 'Яндекс.Маркет — выбор и покупка товаров из проверенных интернет-магазинов'
