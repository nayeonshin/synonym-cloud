from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://google.com")

search_bar = driver.find_element_by_class_name("gLFyf")
search_bar.send_keys("hello!")

driver.quit()
