from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

KEYWORD = "buy domain"  # Temporary
# TODO: KEYWORD strip and make it snake_case

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://google.com")

search_bar = driver.find_element_by_class_name("gLFyf")
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

results = driver.find_element_by_id("rso").find_elements_by_class_name("g")
for index, result in enumerate(results):
    class_name = result.get_attribute("class")
    if "ymu2Hb" not in result.find_element_by_xpath("../../..").get_attribute("class"):
        result.screenshot(f"../screenshots/{KEYWORD}x{index}.png")

# driver.quit()
while True:
    pass
