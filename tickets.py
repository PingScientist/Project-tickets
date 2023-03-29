
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
import time
import ddddocr

d = int(input('場次時間：'))-1
s = int(input('座位區域：'))
n = int(input('輸入票數：'))


driver = webdriver.Chrome()

driver.get("https://tixcraft.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

button = driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
button.click()

activity = driver.find_element(By.XPATH,'//*[@id="activity"]')
activity.click()

theshow = driver.find_element(By.XPATH,'//*[@id="all"]/div[2]/div[20]/div/a')       #choose the activity that you want
location = theshow.location_once_scrolled_into_view
show = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="all"]/div[2]/div[20]/div/a')))     #choose the activity that you want
time.sleep(0.5)
show.click()

buy = driver.find_element(By.CLASS_NAME,'buy')
buy.click()


driver.implicitly_wait(10)
thedate = driver.find_elements(By.CSS_SELECTOR, 'button[class="btn btn-primary text-bold m-0"]')[ｄ] 
location = thedate.location_once_scrolled_into_view
date = driver.find_elements(By.CSS_SELECTOR, 'button[class="btn btn-primary text-bold m-0"]')[ｄ]
date = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-primary text-bold m-0"]')))
date.click()

driver.implicitly_wait(10)
seat = driver.find_elements(By.CSS_SELECTOR, f'[id="13966_{s}"]')
print(seat)
seat = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[id="13966_{s}"]')))
seat.click()

while(True):
    driver.implicitly_wait(10)
    amount = driver.find_element(By.XPATH ,'//*[@id="TicketForm_ticketPrice_01"]')
    amount.click()
    driver.implicitly_wait(10)
    number = driver.find_elements(By.CSS_SELECTOR, 'select option')[n]
    number.click()
    amount.click()

    ###驗證碼處理
    res='AAA'
    while(True):

        element = driver.find_element(By.XPATH,'//*[@id="TicketForm_verifyCode-image"]') # 定位需要截圖的元素

        actions = ActionChains(driver)
        actions.move_to_element(element).perform()       #使用ActionChains類模擬滑鼠操作將頁面滾動至需要截圖的元素

        driver.execute_script("window.scrollBy(0, 100);")   # 使用JavaScript代碼滾動瀏覽器窗口

        element.screenshot('screenshot.png')        # 截圖並保存到指定路徑

        ocr = ddddocr.DdddOcr()

        with open("screenshot.png", 'rb') as f:
            image = f.read()

        res = ocr.classification(image)

        if (len(res)!=4):
            change = driver.find_element(By.XPATH,'//*[@id="TicketForm_verifyCode-image"]')
            change.click()
            time.sleep(0.3)
        else:
            break

    enter_box = driver.find_element(By.CLASS_NAME ,'greyInput')
    enter_box.send_keys(res)
    ###驗證碼處理

    agree = driver.find_element(By.XPATH ,'//*[@id="TicketForm_agree"]')
    agree.click()

    check = driver.find_element(By.XPATH ,'//*[@id="form-ticket-ticket"]/div[4]/button[2]')
    check.click()

    try:
        wait = WebDriverWait(driver, 1)
        alert = wait.until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()
        print(" ")
        print("Alert出現了！")
        print(" ")
        continue
        
    except TimeoutException:
        print(" ")
        print("沒有Alert出現。")
        print(" ")
        break

time.sleep(3)
driver.quit()







