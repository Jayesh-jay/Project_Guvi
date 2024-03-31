import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrangeHRM:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

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
    """

    def add_employee(self, first_name, middle_name, last_name, employee_id):
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click() #Click PIM
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() # Click Add
        self.driver.find_element(By.NAME, "firstName").send_keys(first_name)
        self.driver.find_element(By.NAME, "middleName").send_keys(middle_name)
        self.driver.find_element(By.NAME, "lastName").send_keys(last_name)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys(employee_id)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()

    def edit_employee(self, employee_id, new_first_name):
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click() #click PIM
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(employee_id)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() #click search
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/button[2]").click() #Click edit
        self.driver.find_element(By.NAME, "firstName").clear()
        self.driver.find_element(By.NAME, "firstName").send_keys(new_first_name)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button").click()

    def delete_employee(self, employee_id):
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(employee_id)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/button[1]").click()
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
"""

def test_add_edit_delete_employee():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    orangehrm = OrangeHRM(driver)
    orangehrm.login("Admin", "admin123")

    # Add Employee
    orangehrm.add_employee("John", "", "Doe", "001")
    time.sleep(5)

    # Edit Employee
    orangehrm.edit_employee("001", "Johny")
    time.sleep(5)

    # Delete Employee
    orangehrm.delete_employee("001")
    time.sleep(5)

    driver.quit()


if __name__ == "__main__":
    test_add_edit_delete_employee()
