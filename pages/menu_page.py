from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()


class MenuPage:
    """
    This Page Object represents the left-side hamburger menu in Saucedemo.
    It allows navigation to different sections like All Items, About, Logout, 
    and social media links.
    """
    def __init__(self,driver):
        """
        Store the driver instance and load all menu-related locators from .env.
        """
        self.driver = driver
        self.hamburger_menu = (By.XPATH,os.getenv("MENU_HAMBURGER"))
        self.all_items = (By.LINK_TEXT,os.getenv("MENU_ALL_ITEMS"))
        self.about = (By.LINK_TEXT,os.getenv("MENU_ABOUT"))
        self.logout = (By.LINK_TEXT,os.getenv("MENU_LOGOUT"))
        self.twitter = (By.PARTIAL_LINK_TEXT,os.getenv("MENU_TWITTER"))
        self.facebook = (By.LINK_TEXT,os.getenv("MENU_FACEBOOK"))
        self.linedin = (By.LINK_TEXT,os.getenv("MENU_LINKEDIN"))


    def open_hamberger_menu(self):
        """
        Open the hamburger menu by clicking the menu button.
        """
        self.driver.find_element(*self.hamburger_menu).click()

    def click_all_item(self):
        """
        Click the 'All Items' option in the menu.
        """
        self.driver.find_element(*self.all_items).click()

    def click_about(self):
        """
        Click the 'About' option to navigate to the About page.
        """
        self.driver.find_element(*self.about).click()

    def click_logout(self):
        """
        Click the 'Logout' option to sign out of the application.
        """
        self.driver.find_element(*self.logout).click()

    def click_twitter(self):
        """
        Click the Twitter link from the menu.
        """
        self.driver.find_element(*self.twitter).click()

    def click_facebook(self):
        """
        Click the Facebook link from the menu.
        """
        self.driver.find_element(*self.facebook).click()

    


    
    
