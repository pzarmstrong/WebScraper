from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def airbnb_scrape(url):
    if not "/amenities" in url:
        url = url + "/amenities"
    driver = webdriver.Firefox()
    driver.get(url)
    delay = 3

    try:
        property_name_elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='_fecoyn4']")))
        property_name = property_name_elem.text
    except TimeoutException:
        print("Property name not found in time")
    except NoSuchElementException:
        print("property name element not found with //h1[@class='_fecoyn4']")

    try:
        property_details_elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_tqmy57']")))
        property_details = str.splitlines(property_details_elem.text)
    except TimeoutException:
        print("Property details not found in time")
    except NoSuchElementException:
        print("property details element not found with //div[@class='_tqmy57']")

    try:
        amenities_elem = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='_gw4xx4']")))
    except TimeoutException:
        print("Amenities not found in time")
    except NoSuchElementException:
        print("amenities element not found with //div[@class='_gw4xx4']")

    property_type = str.split(property_details[0], " hosted ")[0]
    num_bedrooms = property_details[3]
    num_bathrooms = property_details[7]

    amenities = []

    for amens in amenities_elem:
        if "Unavailable" in amens.text:
            continue
        amenities.append(amens.text)

    print("property name: " + property_name)
    print("property type: " + property_type)
    print("number of bedrooms: " + num_bedrooms[2:])
    print("number of bathrooms: " + num_bathrooms[2:])
    print("amenities:")
    print(*amenities, sep=", ")
    print("\n####\t####\t####\n")

print("\n####\t####\t####\n")
airbnb_scrape("https://www.airbnb.co.uk/rooms/50633275")
airbnb_scrape("https://www.airbnb.co.uk/rooms/33090114")
airbnb_scrape("https://www.airbnb.co.uk/rooms/52202994")
airbnb_scrape("https://www.airbnb.co.uk/rooms/13126329")
airbnb_scrape("https://www.airbnb.co.uk/rooms/17810191")