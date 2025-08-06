from selenium.webdriver.common.by import By


class MenuPage:
    def __init__(self,driver):
        self.driver = driver
        self.hamburger_menu = (By.XPATH,"//div[@class='bm-burger-button']")
        self.all_items = (By.LINK_TEXT,"All Items")
        self.about = (By.LINK_TEXT,"About")
        self.logout = (By.LINK_TEXT,"Logout")
        self.twitter = (By.PARTIAL_LINK_TEXT,"Twitter")
        self.facebook = (By.LINK_TEXT,"Facebook")
        self.linedin = (By.LINK_TEXT,"LinkedIn")


    def open_hamberger_menu(self):
        self.driver.find_element(*self.hamburger_menu).click()

    def click_all_item(self):
        self.driver.find_element(*self.all_items).click()

    def click_about(self):
        self.driver.find_element(*self.about).click()

    def click_logout(self):
        self.driver.find_element(*self.logout).click()

    def click_twitter(self):
        self.driver.find_element(*self.twitter).click()

    def click_facebook(self):
        self.driver.find_element(*self.facebook).click()

    


    
    
