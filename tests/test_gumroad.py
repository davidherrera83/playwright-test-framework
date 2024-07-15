from fw import Locator


def test_gumroad_search_by_store(gumroad):
    # Visit https://gumroad.com and search for the creator 'easlo'. 
    gumroad.visit_gumroad()
    gumroad.search("easlo")
    # Wait for search to complete, get the user name of the first product card and verify the creator name 'Easlo' in product card
    gumroad.wait_for_element_load(Locator.USER)
    user_text = gumroad.get_text_from_element(".user")
    assert "Easlo" in user_text

def test_add_item_to_cart(gumroad):
    # Visit https://gumroad.com and verify product cards are present
    gumroad.visit_gumroad()
    gumroad.wait_for_element_load(Locator.PRODUCT_CARD)
    # Get all producr cards and select the third product
    products = gumroad.get_elements(Locator.PRODUCT_CARD)
    third_product = products[2] 
    third_product.click()
    # Obtain the item name, click add to cart, verify that 
    gumroad.wait_for_element_load(Locator.ITEM_NAME)
    item_name = gumroad.get_text_from_element(Locator.ITEM_NAME)
    gumroad.click_element(Locator.ADD_TO_CART)
    assert "checkout" in gumroad.get_current_url()
    gumroad.wait_for_element_load(f"text={item_name}")
    assert item_name in gumroad.get_text_from_element(f"text={item_name}")
