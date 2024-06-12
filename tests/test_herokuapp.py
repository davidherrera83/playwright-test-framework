import re
from playwright.sync_api import Page, expect
from fw import Examples

def test_visit_herokuapp(herokuapp, page: Page):
    herokuapp.visit_herokuapp()
    expect(page).to_have_title(re.compile("The Internet"))

def test_click_on_example(herokuapp, page: Page):
    herokuapp.visit_herokuapp()
    herokuapp.click_on_example(Examples.ADD_REMOVE_ELEMENTS)
    expect(page).to_have_url(re.compile(".*add_remove_elements/"))
