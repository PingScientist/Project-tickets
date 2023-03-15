from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://tixcraft.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

button = driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
button.click()

activity = driver.find_element(By.XPATH,'//*[@id="activity"]')
activity.click()

theshow = driver.find_element(By.XPATH,'//*[@id="all"]/div[2]/div[10]/div/a')       #choose the activity that you want
location = theshow.location_once_scrolled_into_view
show = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="all"]/div[2]/div[10]/div/a')))     #choose the activity that you want
show.click()

buy = driver.find_element(By.CLASS_NAME,'buy')
buy.click()

driver.implicitly_wait(10)
thedate = driver.find_elements(By.CSS_SELECTOR, 'button[class="btn btn-primary text-bold m-0"]')[0]
location = thedate.location_once_scrolled_into_view
date = driver.find_elements(By.CSS_SELECTOR, 'button[class="btn btn-primary text-bold m-0"]')[0]
date = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-primary text-bold m-0"]')[0]))

date.click()

time.sleep(10)
'''
//*[@id="gameList"]/table/tbody/tr[1]/td[4]/button
//*[@id="gameList"]/table/tbody/tr[2]/td[4]/button
'''
'''
//*[@id="group_0"]/li[1]
//*[@id="group_0"]/li[3]
//*[@id="group_1"]/li[1]
//*[@id="group_2"]/li[3]
'''






