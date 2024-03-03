import logging
import time
import random
from selenium import webdriver  # Import SeleniumWire instead of regular webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

uas = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.119 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.119 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPod; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.119 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36"
]


class HeadlessBrowser:
    def __init__(self, proxy_address=None, cf=False):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.ua = random.choice(uas)
        self.driver = self.launch_headless_browser(proxy_address, cf)

    def launch_headless_browser(self, proxy_address=None, cf=False):
        chrome_options = Options()
        user_agent = self.ua
        chrome_options.add_argument(f'--user-agent={user_agent}')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--log-level=3')

        if cf:
            chrome_options.add_extension('cf.crx')

        if proxy_address:
            chrome_options.add_argument(f'--proxy-server={proxy_address}')
            driver = webdriver.Chrome(options=chrome_options)
        else:
            driver = webdriver.Chrome(options=chrome_options)

        return driver

    def is_page_loaded(self, url, timeout=30):
        self.logger.info(f"Checking if the page at {url} has loaded...")

        try:
            self.driver.get(url)
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )

            # Check HTTP response status using JavaScript
            response_status = self.driver.execute_script("return window.performance.timing.responseEnd")
            return response_status >= 0
        except Exception as e:
            self.logger.error(f"Error checking if the page loaded: {e}")
            return False

    def launch(self, url):
        self.driver.get(url)

    def wait_for_seconds(self, seconds=10):
        time.sleep(seconds)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def reload(self):
        self.driver.refresh()

    def print_page_text(self):
        page_text = self.driver.find_element(By.TAG_NAME, 'body').text
        return page_text

    def get_cook(self):
        all_cookies = self.driver.get_cookies()
        cookies_dict = {}
        for cookie in all_cookies:
            cookies_dict[cookie['name']] = cookie['value']
        return cookies_dict
        
    def close(self):
        self.driver.quit()
