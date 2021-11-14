from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class GoogleKeywordScreenshotTaker:
    def __init__(self, search_term):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.search_term = search_term

    def start(self):
        self.driver.get("https://google.com")
        search_bar = self.driver.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.search_term)
        search_bar.send_keys(Keys.ENTER)

        try:
            next_page_button = self.driver.find_element_by_id("pnnext")

            count = 0
            while next_page_button:
                if count > 9:
                    break

                results = self.driver.find_element_by_id("rso").find_elements_by_class_name(
                    "g"
                )
                for index, result in enumerate(results):
                    class_name = result.get_attribute("class")
                    if "ymu2Hb" not in result.find_element_by_xpath(
                        "../../.."
                    ).get_attribute("class"):
                        replaced_search_term = self.search_term.replace(" ", "_")
                        result.screenshot(
                            f"screenshots/{replaced_search_term}x{count}x{index}.png"
                        )

                next_page_button.click()
                next_page_button = self.driver.find_element_by_id("pnnext")
                count += 1
        except AttributeError:
            print("No results")

    def finish(self):
        self.driver.quit()
