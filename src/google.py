from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class GoogleKeywordScreenShooter:
    def __init__(self, search_term):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.search_term = search_term

    def start(self):
        self.driver.get("https://google.com")
        search_bar = self.driver.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.search_term)
        search_bar.send_keys(Keys.ENTER)

        try:
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
                        f"../screenshots/{replaced_search_term}x{index}.png"
                    )
        except AttributeError:
            print("No results")

    def finish(self):
        self.driver.quit()


shooter = GoogleKeywordScreenShooter("dog")  # TODO: Replace hardcoded user input
shooter.start()
shooter.finish()
