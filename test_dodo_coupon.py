from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure
from allure import severity, severity_level


@allure.title('Применение купона')
@severity(severity_level.CRITICAL)
def test_dodo_coupon():
    driver = WebDriver(executable_path='C://Chrome driver 84/chromedriver.exe')
    with allure.step('Открываем главную страницу'):
        driver.get('https://dodopizza.ru/moscow/')
        assert driver.title == '🍕 Додо Пицца Москва | Сеть пиццерий №1 в России'

    with allure.step('Выбираем товар'):
        target_item = driver.find_element_by_xpath('//img[@title="Магнат"]')
        actions = ActionChains(driver)
        actions.move_to_element(target_item)
        target_item.click()

    with allure.step('Добавляем товар в корзину'):
        add_to_cart = driver.find_element_by_xpath('//button[@class="sc-91ilwk-0 sc-1y25m1i-23 eDpWH"]')
        add_to_cart.click()
        WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-quantity="2"]'))
        )

    with allure.step('Переходим в корзину'):
        cart = driver.find_element_by_xpath('//button[text()="Корзина"]')
        cart.click()
        WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//h2[text()="Промокод"]'))
        )

    with allure.step('Вводим прокомод'):
        coupon_field = driver.find_element_by_xpath('//input[@data-testid="promocode__input"]')
        coupon_field.send_keys("9380")

    with allure.step('Нажимаем на кнопку применить'):
        code_applying = driver.find_element_by_xpath('//button[text()="Применить"]')
        code_applying.click()

    with allure.step('Проверяем, что промокод применился'):
        WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="promocode__control"]'))
        )