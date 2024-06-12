import re
from playwright.sync_api import Page

class HerokuApp:
    def __init__(self, page: Page) -> None:
        self.page = page

    def visit_herokuapp(self):
        self.page.goto("https://the-internet.herokuapp.com/")

        return self
    
    def click_on_example(self, available_example: str):
        self.page.click(f'a[href="{available_example}"]')

        return self