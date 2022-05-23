import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver.exe')
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))
driver.get('https://www.linkedin.com/login/es')

driver.find_element(by=By.ID,value='username').send_keys('ricardojlopez981@gmail.com')
driver.find_element(by=By.ID, value='password').send_keys('0cb1e57a1')
driver.find_element(by=By.ID, value='password').submit()

time.sleep(5)
driver.find_element(by=By.XPATH,value='//header/div[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Applaudo Studios')
driver.find_element(by=By.XPATH,value='//header/div[1]/div[1]/div[1]/div[1]/input[1]').send_keys(Keys.ENTER)

time.sleep(3)
driver.find_element(by=By.LINK_TEXT,value='Applaudo Studios').click()

# Making scroll to the page
driver.execute_script("window.scrollTo(0, 50)")

# Making a wait before click the button
# wait = WebDriverWait(driver, 30) # timeout in seconds -> 30
# wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "body.system-fonts:nth-child(2) main.app__content:nth-child(2) div.card-layout:nth-child(5) div:nth-child(1) form.login__form div.login__form_action_container:nth-child(29) > button.btn__primary--large.from__button--floating")))
