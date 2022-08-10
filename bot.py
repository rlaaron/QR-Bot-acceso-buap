import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



url = 'https://accesoqr.buap.mx/'
user = 'email'
psw = 'password'

login = '#__next > main > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-elevation6.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-sm-8.MuiGrid-grid-md-5.css-1qupdea > div > form > button.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-fullWidth.MuiButtonBase-root.css-g256t'
# login = '/html/body/div/main/div[2]/div/form/button[1]'
# userButtom = '#i0116'
userButtom = '//*[@id="i0116"]'
nextButtom = '#idSIButton9'
passwordButtom = '#i0118'
startButtom = '#idSIButton9'
safeSesion = '#idBtn_Back'

#form

vaccination = 'body > div.MuiModal-root.MuiDialog-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > form > div.MuiDialogContent-root.css-1ty026z > div > div:nth-child(3) > div > label > span.MuiSwitch-root.MuiSwitch-sizeMedium.css-1oaxxy6 > span.MuiSwitch-switchBase.MuiSwitch-colorPrimary.MuiButtonBase-root.MuiSwitch-switchBase.MuiSwitch-colorPrimary.PrivateSwitchBase-root.css-4vfax9 > input'
accept = 'body > div.MuiModal-root.MuiDialog-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > form > div.MuiDialogContent-root.css-1ty026z > div > div:nth-child(5) > div > fieldset > label > span.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiButtonBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.PrivateSwitchBase-root.css-17ki52k > input'
confirm = 'body > div.MuiModal-root.MuiDialog-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > form > div.MuiDialogActions-root.MuiDialogActions-spacing.css-14b29qc > button.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButtonBase-root.css-lbgtqn'
close = 'body > div.MuiModal-root.MuiDialog-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > div.MuiDialogActions-root.MuiDialogActions-spacing.css-14b29qc > button'

#download
dowload = '#__next > div > main > main > div > div > div > div > a'
dowload2 = '#icon > iron-icon'

driverPath = "C:\\Users\\aaron\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
# driverPath = 'C:\\Users\\aaron\\Downloads\\chromedriver_win32 (1)'

driver = webdriver.Chrome(driverPath)

driver.get(url)


# driver.find_element(By.XPATH,(login)).click()
driver.find_element(By.CSS_SELECTOR,(login)).click()
time.sleep(2)
driver.find_element(By.XPATH,(userButtom)).send_keys(user)
driver.find_element(By.CSS_SELECTOR,(nextButtom)).click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,(passwordButtom)).send_keys(psw)
driver.find_element(By.CSS_SELECTOR,(startButtom)).click()
driver.find_element(By.CSS_SELECTOR,(safeSesion)).click()
time.sleep(2)
print('todo good')
if driver.find_element(By.CSS_SELECTOR,(dowload)):
    driver.find_element(By.CSS_SELECTOR,(dowload)).click()
    print('ya se ha relizado el formulario')
else:
    print('no se ha relizado el formulario')
    driver.find_element(By.CSS_SELECTOR,(vaccination)).click()
    driver.find_element(By.CSS_SELECTOR,(vaccination)).click()
    driver.find_element(By.CSS_SELECTOR,(accept)).click()
    driver.find_element(By.CSS_SELECTOR,(confirm)).click()
    driver.find_element(By.CSS_SELECTOR,(close)).click()

driver.save_screenshot('qr.png')

time.sleep(2)


print('Done')
