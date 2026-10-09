import time

from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Single Iframe:
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
# single_frame=driver.find_element(By.XPATH,'//div[@id="Single"]/iframe')
# driver.switch_to.frame(single_frame)
driver.switch_to.frame("singleframe")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hello World")
driver.switch_to.default_content()


# Nested IFrame:
driver.find_element(By.XPATH,"//*[text()='Iframe with in an Iframe']").click()
parent_frame=driver.find_element(By.XPATH,"//div[@id='Multiple']/iframe")
# parent_frame=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(parent_frame)
time.sleep(2)
child_frame=driver.find_element(By.XPATH,"//div[@class='iframe-container']/iframe ")
driver.switch_to.frame(child_frame)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hello World")
driver.switch_to.default_content()
