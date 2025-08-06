from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID,"user-name")
        self.password = (By.ID,"password")
        self.login_btn = (By.ID,"login-button")
        self.error_message_= (By.CSS_SELECTOR, ".error-message-container.error")

    def open(self,baseUrl):
        self.driver.get(baseUrl)


    # def login(self, username, password):
        # self.driver.find_element(By.ID, "user-name").send_keys(username)
        # self.driver.find_element(By.ID, "password").send_keys(password)
        # self.driver.find_element(By.ID, "login-button").click()

    # def get_error(self):
    #     return self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text



    def enter_username(self,username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def error_message(self):
        return self.driver.find_element(*self.error_message_).text
    
    def login(self,username,password):
        if username:
            self.enter_username(username)

        if password:
            self.enter_password(password)

        self.click_login()
    

