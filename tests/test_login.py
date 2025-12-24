from selenium.webdriver.common.by import By

def test_successful_login(browser):
    browser.get("https://the-internet.herokuapp.com/login")

    browser.find_element(By.ID, "username").send_keys("tomsmith")
    browser.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    logout_button = browser.find_element(By.CSS_SELECTOR, "a.button.secondary.radius")
    assert logout_button.is_displayed()
