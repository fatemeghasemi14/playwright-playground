import time

from playwright.sync_api import Page, expect

def test_priceEquality(page: Page):
    # Check the price of rice is equal to 37.
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            priceColumnValue = index
            newColumnValue = priceColumnValue + 1
            break
    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator(f"td:nth-child({newColumnValue})")).to_have_text("37")


def test_lastTable(page: Page):
    # validate apple discount price is 41.
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    page.get_by_role("button", name="Last").click()
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Discount price").count() > 0:
            discountColumnValue = index + 1
            break

    appleTr = page.locator("tr").filter(has_text="Apple")
    expect(appleTr.locator(f"td:nth-child({discountColumnValue})")).to_have_text("41")


def test_pageSize5(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    page.get_by_role("combobox").select_option("10")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColumnValue = index + 1
            break
    guavaTr = page.locator("tr").filter(has_text="Guava")
    expect(guavaTr.locator(f"td:nth-child({priceColumnValue})")).to_have_text("42")
