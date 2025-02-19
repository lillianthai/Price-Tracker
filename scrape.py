from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import re


URL = "https://www.yesstyle.com/en/miseensc%C3%A9ne-perfect/info.html/pid.1086718411"
#URL = "https://www.chemistwarehouse.com.au/buy/91329/cerave-moisturising-cream-454g"

options = webdriver.FirefoxOptions()
options.add_argument("--headless=new")

driver = webdriver.Firefox(options=options)
driver.get(URL)

# Find the element containing the price data

# yesstyle
if (URL.startswith("https://www.yesstyle.com")):
    product_data = driver.find_element(By.CSS_SELECTOR, ".productDetailPage_sellingPrice__s6PZu").get_attribute('innerHTML')
# chemist warehouse
elif (URL.startswith("https://www.chemistwarehouse.com.au")):
    product_data = driver.find_element(By.CSS_SELECTOR, ".Price").get_attribute('innerHTML')


# Extract the price using regex
price = re.findall(r"\d+\.\d+", product_data)[0]

print(price)

# convert string to float
price_value = float(price)

driver.quit()

