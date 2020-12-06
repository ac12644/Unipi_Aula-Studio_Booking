from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from selenium.webdriver.common.alert import Alert




driver = webdriver.Chrome()
driver.get('https://agende.unipi.it/lfm-snn-wpj')   # AULA STUDIO PACINOTTI
 
inputElems = driver.find_elements_by_id('i0116')
 
for inputElem in inputElems:
     inputElem.send_keys('aa@unipi.it')
     inputElem.send_keys(Keys.ENTER)
 
usernameStr = 'YOUR_USERNAME'   #c ALICE CREDENTIALS
passwordStr = 'PASSWORD'
 
username = WebDriverWait(driver, 30).until(
     EC.presence_of_element_located((By.ID, 'username')))
username.send_keys(usernameStr)
 
password = driver.find_element_by_id('password')
password.send_keys(passwordStr)
 
 
nextButton = driver.find_element_by_name('_eventId_proceed')
nextButton.click()
yesButton = WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.ID,'idSIButton9')))
yesButton.click()

monthButton = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,('//*[@id="calendar"]/div[1]/div[3]/div/button[1]'))))

monthButton.click()
    #  sunday 6, monday 0 , tue 1, wed 2, thur 3, fri 4, sat 5
if date.today().weekday() == 1:
    
     bookButton = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH,('/html/body/div/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/a/div'))))
     bookButton.click()
     
     bookButton2 = driver.find_element_by_xpath('/html/body/div/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/a/div')
     bookButton2.click()

if date.today().weekday() == 2:

    bookButton = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH,('/html/body/div[1]/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/a/div'))))
    bookButton.click()

    bookButton2 = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[2]/td[4]/a/div')
    bookButton2.click()

if date.today().weekday() == 3:
    
    bookButton = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH,('/html/body/div[1]/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/a/div'))))
    bookButton.click()

    bookButton2 = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[2]/td[5]/a/div')
    bookButton2.click()

if date.today().weekday() == 4:

    bookButton = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH,('/html/body/div[1]/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[1]/td[6]/a/div'))))
    bookButton.click()

    bookButton2 = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[2]/td[6]/a/div')
    bookButton2.click()
    
    bookButton3 = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[1]/td[7]/a/div')
    bookButton2.click()

    bookButton4 = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[2]/td[7]/a/div')
    bookButton2.click()

if date.today().weekday() == 6:
    
    bookButton = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH,('/html/body/div/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr[1]/td[1]/a/div'))))
    bookButton.click()

    bookButton2 = driver.find_element_by_xpath('/html/body/div/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr[2]/td[1]/a/div')
    bookButton2.click()

    bookButton3 = driver.find_element_by_xpath('/html/body/div/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/a/div')
    bookButton2.click()

    bookButton4 = driver.find_element_by_xpath('/html/body/div/section/div/div/div/div/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/a/div')
    bookButton2.click()

else:
    print("DAYS DO N0T MATCH OR SOMETHING WRONG")

    
