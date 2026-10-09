from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains, keys_to_typing

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/")
driver.maximize_window()

mail_id= driver.find_element(By.ID,"email")
actions = ActionChains(driver)
actions.move_to_element(mail_id).perform()
actions.send_keys(Keys.SHIFT).send_keys("testmail").send_keys(Keys.SHIFT).perform()
sign_up= driver.find_element(By.ID,"enterimg")
actions.move_to_element(sign_up).perform()

def test_verify_logo(browser):
    browser.get("https://demo.automationtesting.in/Register.html")

    logo = browser.find_element(By.XPATH,"//*[contains(text(), 'Automation Demo Site')]")
    assert logo.is_displayed(), "Logo is visible on the webpage"




