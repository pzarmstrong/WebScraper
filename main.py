from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webelement import FirefoxWebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Firefox();
driver.get('https://www.airbnb.co.uk/rooms/33090114/amenities');

propertyname = driver.find_element(By.XPATH, "//meta[@property='og:title']").get_attribute('content');

print(propertyname);