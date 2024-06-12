import pytest
from playwright.sync_api import Page
from the_internet.herokuapp import HerokuApp

@pytest.fixture
def herokuapp(page: Page) -> HerokuApp:
    """Instance of HerokuApp for each test."""
    return HerokuApp(page)