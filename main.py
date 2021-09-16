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
    print("property type: " + property_type)
    print("number of bedrooms: " + num_bedrooms)
    print("number of bathrooms: " + num_bathrooms)
    print("amenities:")
    print(*amenities, sep=", ")
    print("\n####\t####\t####\n")

airbnb_scrape("https://www.airbnb.co.uk/rooms/50633275")
airbnb_scrape("https://www.airbnb.co.uk/rooms/33090114")
airbnb_scrape("https://www.airbnb.co.uk/rooms/52202994")