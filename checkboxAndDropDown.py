from asyncio import wait

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demo.automationtesting.in/Register.html')
driver.maximize_window()

li= driver.find_elements(By.XPATH,"//*[@type='checkbox']")
for ele in li:
    val=ele.get_attribute('value')
    print(val)
    if val =="Hockey":
        ele.click()

select_dr = driver.find_element(By.ID,"Skills")
sel=Select(select_dr)
sel.select_by_value("Analytics")
