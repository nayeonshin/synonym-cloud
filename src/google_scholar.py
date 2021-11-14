import time
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


test_data = ["dog", "hound", "canine", "pup", "puppy"]
driver = webdriver.Chrome(ChromeDriverManager().install())


result_dict = {}

driver.get("https://scholar.google.com")

def find_num (result_str):
	num = 0
	if result_str ==  "":
		num = 0
		return num
	result_split = result_str.split(" ")
	num = int(result_split[1].replace(",", ""))

	return num

def scholar_results(synonyms):
	result_dict = {}

	for word in synonyms:
		#navigate to search bar
		search_bar = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='q']")))
		#enter in data
		search_bar.clear()
		search_bar.send_keys(word)
		search_button = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
		print(word)

		#get the number of results 
		num_results_str = driver.find_element(By.ID, "gs_ab_md").text
		num_results = find_num(num_results_str)
		print(num_results)

		#add to dictionary
		result_dict[word] = num_results


	return result_dict

#testing
test_dict = scholar_results(test_data)

print(test_dict)


	





while(True):
    pass
