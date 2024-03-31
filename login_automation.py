import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginAutomation:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)  # Setting implicit wait to 10 seconds

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def inputBox(self, value, key):
        self.driver.find_element(By.NAME, value).send_keys(key)

    def submitBtn(self):
        self.driver.find_element(By.TAG_NAME, "button").click()

    def quit(self):
        self.driver.quit()

    def login(self):
        self.boot()
        self.inputBox("username", self.username)
        self.inputBox("password", self.password)
        self.submitBtn()
        try:
            WebDriverWait(self.driver, 5).until(EC.url_contains("dashboard"))  # Wait until dashboard URL is loaded
            print("Login Successful")
            return True
        except:
            print("Invalid credentials")
            return False

@pytest.fixture(scope="function")
def login_automation():
    url = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    obj = LoginAutomation(url, username, password)
    yield obj
    obj.quit()

def test_login_successful(login_automation):
    assert login_automation.login(), "Login unsuccessful"
    print("Login successful")

def test_login_invalid_credentials(login_automation):
    login_automation.username = "Admin"
    login_automation.password = "invalid_password"
    assert not login_automation.login(), "Invalid credentials allowed login"
