import config
from utils import pause
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from decorators import log_decorator
from typing import List


class Driver:
    def __init__(self):
        """
        Initializes a new instance of the Driver class with a null WebDriver instance.
        """
        self.driver = None

    @log_decorator
    def start_driver(self) -> None:
        """
        Starts the WebDriver instance.
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--log-level=3")

        # Go headless
        if config.HEADLESS:
            options.add_argument("--headless")

        # Provide the path of chromedriver present on your system.
        self.driver = webdriver.Chrome(executable_path="chromedriver", options=options)

    @log_decorator
    def get_driver(self) -> webdriver:
        """
        Gets the WebDriver instance.

        Returns:
            WebDriver: The WebDriver instance.
        """
        return self.driver

    @log_decorator
    def quit_driver(self) -> None:
        """
        Quits the WebDriver instance.
        """
        self.driver.quit()


class Bot:
    def __init__(self, driver):
        self.driver = driver
        self.username = config.USERNAME
        self.password = config.PASSWORD
        self.target_account = config.TARGET_ACCOUNT

        self.target_account_followers: List[str] = []
        self.target_account_following: List[str] = []

    @log_decorator
    def get_url(self, url: str) -> None:
        self.driver.get(url)
        pause()

    @log_decorator
    def run(self) -> None:
        url = f"https://www.instagram.com/{self.target_account}/"
        self.get_url(url)

        followers_element = self.driver.find_element(
            By.XPATH, "//span[@title='followers']"
        )
        followers_count = followers_element.get_attribute("title")

        print(followers_count)


# Main Function
if __name__ == "__main__":
    driver = Driver()
    driver.start_driver()

    bot = Bot(driver.get_driver())
    bot.run()

    driver.quit_driver()
