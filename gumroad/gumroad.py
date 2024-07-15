from playwright.sync_api import Page


class GumroadApp:
    def __init__(self, page: Page):
        self.page = page

    def visit_gumroad(self):
        self.page.goto("https://gumroad.com")

        return self

    def search(self, search_value: str):
        self.page.fill("input[role='combobox']", f"{search_value}")
        self.page.press("input[role='combobox']", "Enter")

        return self

    def wait_for_element_load(self, css_selector: str):
        self.page.wait_for_selector(f"{css_selector}")

        return self

    def get_text_from_element(self, css_selector: str) -> str:
        element_text = self.page.text_content(f"{css_selector}")

        return element_text

    def get_elements(self, css_selector: str):
        elements = self.page.query_selector_all(css_selector)

        return  elements
    
    def click_element(self, css_selector: str):
        self.page.click(css_selector)

        return self
    
    def get_current_url(self) -> str:
        current_url = self.page.url

        return current_url