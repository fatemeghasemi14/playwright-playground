import time

from playwright.sync_api import Page


# Validate the price of rice is equal to 37
def test_ricepriceChecking(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    columnHeaders = page.locator("th")
    for i in range(columnHeaders.count()):
        if columnHeaders.nth(i).text_content().strip() == "Price":
            priceHeader = i
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
    assert riceRow.locator("td").nth(priceHeader).text_content().strip() == "37"



# Validate the discount of Tomato is equal to 26.
def test_tomatoDiscountChecking(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    page.get_by_role("combobox").select_option("20")
    page.get_by_label("Search:").fill("o")
    columnHeaders = page.locator("th")
    for i in range(columnHeaders.count()):
        if columnHeaders.nth(i).text_content().strip() == "Discount price":
            discountPriceHeader = i
            break

    tomatoRow = page.locator("tr").filter(has_text="Tomato")
    assert tomatoRow.locator("td").nth(discountPriceHeader).text_content().strip() == "26"



