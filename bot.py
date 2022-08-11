# Importing the libraries that are used in the script.
from tabnanny import check
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from decouple import config

# url of the page
url = 'https://accesoqr.buap.mx/' 


# Using the `decouple` library to get the email, password and form from a `.env` file.
user = config('email') 
psw = config('password')
complete = config('form')

# Using the `selenium` library to open the browser and navigate to the page.
# login to the page
login = '#__next > main > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-elevation6.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-sm-8.MuiGrid-grid-md-5.css-1qupdea > div > form > button.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-fullWidth.MuiButtonBase-root.css-g256t'
# input for the email
userButtom = '#i0116'
# button to confirm the session
nextButtom = '#idSIButton9'
# input for the password
passwordButtom = '#i0118'
# button to confirm the session
startButtom = '#idSIButton9'
# button to confirm safe session
safeSesion = '#idBtn_Back'

# fill form

# full vaccination
vaccination = 'body > div.MuiModal-root.MuiDialog-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > form > div.MuiDialogContent-root.css-1ty026z > div > div:nth-child(3) > div > label > span.MuiSwitch-root.MuiSwitch-sizeMedium.css-1oaxxy6 > span.MuiSwitch-switchBase.MuiSwitch-colorPrimary.MuiButtonBase-root.MuiSwitch-switchBase.MuiSwitch-colorPrimary.PrivateSwitchBase-root.css-4vfax9 > input'
# accept tell the truth
accept = 'body > div.MuiModal-root.MuiDialog-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > form > div.MuiDialogContent-root.css-1ty026z > div > div:nth-child(5) > div > fieldset > label > span.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiButtonBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.PrivateSwitchBase-root.css-17ki52k > input'
# button to confirm the form
confirm = 'body > div.MuiModal-root.MuiDialog-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > form > div.MuiDialogActions-root.MuiDialogActions-spacing.css-14b29qc > button.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButtonBase-root.css-lbgtqn'
# close the form
close = 'body > div.MuiModal-root.MuiDialog-root.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > div.MuiDialogActions-root.MuiDialogActions-spacing.css-14b29qc > button'

#download qr optional
# dowload = '#__next > div > main > main > div > div > div > div > a'

# path to the chromedriver
driverPath = "C:\\Users\\aaron\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"

# open the browser
driver = webdriver.Chrome(driverPath)

# navigate to the page
driver.get(url)




# A way to find the element in the page and click it.
driver.find_element(By.CSS_SELECTOR,(login)).click()
time.sleep(1) # wait 1 seconds to load the page
driver.find_element(By.CSS_SELECTOR,(userButtom)).send_keys(user)
driver.find_element(By.CSS_SELECTOR,(nextButtom)).click()
driver.find_element(By.CSS_SELECTOR,(passwordButtom)).send_keys(psw)
time.sleep(.5) # wait 0.5 seconds to load the page
driver.find_element(By.CSS_SELECTOR,(startButtom)).click()
driver.find_element(By.CSS_SELECTOR,(safeSesion)).click()
# finish the login

# wait for the form to load
time.sleep(1.5)




# Checking if the form is complete. If it is complete, it will download the QR code. If it is not
# complete, it will fill the form.
if complete:
    
    time.sleep(.5)
    # driver.find_element(By.CSS_SELECTOR,(dowload)).click() # download the QR code optional
    driver.save_screenshot('qr.png') # save the QR code optional
    driver.close() # close the browser

else:
    driver.find_element(By.CSS_SELECTOR,(vaccination)).click()
    driver.find_element(By.CSS_SELECTOR,(vaccination)).click()
    driver.find_element(By.CSS_SELECTOR,(accept)).click()
    driver.find_element(By.CSS_SELECTOR,(confirm)).click()
    time.sleep(.5)
    driver.find_element(By.CSS_SELECTOR,(close)).click()
    time.sleep(.5)
    driver.save_screenshot('qr.png') # save the QR code optional
    driver.close() # close the browser

# end of the program

print('Done')
