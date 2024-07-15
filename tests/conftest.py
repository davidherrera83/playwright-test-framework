import pytest
from playwright.sync_api import Page
from gumroad.gumroad import GumroadApp

@pytest.fixture
def gumroad(page: Page) -> GumroadApp:
    """Instance of GumroadApp for each test."""
    _gumroad = GumroadApp(page)
    return _gumroad