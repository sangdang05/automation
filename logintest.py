from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


url = "https://www.saucedemo.com/"

class Logintest():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver =  webdriver.Chrome(options=chrome_options)

    def open_browser(self):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
        except Exception as e:
            print(e)

    def fill_username(self, value):
        uername = self.driver.find_element(by=By.ID, value="user-name")
        uername.send_keys(value)

    def fill_password(self, value):
        password = self.driver.find_element(by=By.ID, value="password")
        password.send_keys(value)

    def login_btn(self):
        btn = self.driver.find_element(by=By.ID, value="login-button")
        btn.click()
        # self.driver.implicitly_wait(10)

    def login_successful(self):
        app_logo = self.driver.find_element(by=By.CLASS_NAME, value="app_logo")
        tille = self.driver.find_element(by=By.XPATH, value="//span[@class='title']")
        assert app_logo.is_displayed()
        assert tille.is_displayed()
        self.driver.close()

    def login_fail(self, err_value):
        err_message = self.driver.find_element(by=By.XPATH, value="//h3[contains(@data-test,'error')]").text
        if err_message == err_value:
            print("pass")
        else:
            print("failed")


loginTsc = Logintest()
def Verify_that_login_successfully_with_valid_value():
    loginTsc.open_browser()
    loginTsc.fill_username(value="standard_user")
    loginTsc.fill_password(value="secret_sauce")
    loginTsc.login_btn()
    loginTsc.login_successful()

def Verify_that_login_failed_with_an_invalid_value():
    loginTsc.open_browser()
    loginTsc.fill_username(value="standard_user1")
    loginTsc.fill_password(value="secret_sauce1")
    loginTsc.login_btn()
    loginTsc.login_fail(err_value="Epic sadface: Username and password do not match any user in this service")

def Verify_that_login_unsuccessfully_when_leaving_blank_Username_and_Password_field():
    loginTsc.open_browser()
    loginTsc.fill_username(value="")
    loginTsc.fill_password(value="")
    loginTsc.login_btn()
    loginTsc.login_fail(err_value="Epic sadface: Username is required")
    


if __name__ == "__main__":
    #Verify_that_login_successfully_with_valid_value()
    #Verify_that_login_failed_with_an_invalid_value()
    Verify_that_login_unsuccessfully_when_leaving_blank_Username_and_Password_field()
    


