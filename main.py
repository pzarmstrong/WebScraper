from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webelement import FirefoxWebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import string


driver = webdriver.Firefox()
driver.get('https://www.airbnb.co.uk/rooms/33090114/amenities')
delay = 3

try:
    property_name_elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='_fecoyn4']")))
    property_name = property_name_elem.text
except TimeoutException:
    print("Property name not found in time")

# property_details = driver.find_element(By.XPATH, "//div[@class='_tqmy57']");
try:
    property_details_elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_tqmy57']")))
    property_details = str.splitlines(property_details_elem.text)
except NoSuchElementException:
    print("Property details not found in time")

try:
    amenities_elem = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='_gw4xx4']")))
except TimeoutException:
    print("Amenities not found in time")

property_type = str.split(property_details[0], " hosted ")[0]
num_bedrooms = property_details[3]
num_bathrooms = property_details[7]

amenities = []

for amens in amenities_elem:
    if "Unavailable" in amens.text:
        continue
    amenities.append(amens.text)


print("property name: " + property_name)
print("\nproperty type: " + property_type)
print("\nnumber of bedrooms: " + num_bedrooms)
print("\nnumber of bathrooms: " + num_bathrooms)
print("\namenities:")
print(*amenities, sep=", ")