import time

from playwright.sync_api import Page, expect

def test_selectFruitsRandomly(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    brocolliProduct = page.locator(".product").filter(has_text="Brocolli - 1 Kg")
    brocolliPrice = int(brocolliProduct.locator(".product-price").text_content())
    brocolliProduct.get_by_role("button", name="ADD TO CART").click()
    beetrootProduct = page.locator(".product").filter(has_text="Beetroot - 1 Kg")
    beetrootPrice = int(beetrootProduct.locator(".product-price").text_content())
    beetrootProduct.get_by_role("button", name="ADD TO CART").click()
    totalPrices = brocolliPrice + beetrootPrice
    page.locator("img[alt='Cart']").click()
    page.get_by_role("button", name="PROCEED TO CHECKOUT").click()
    totalAmount = int(page.locator(".totAmt").text_content())
    assert totalPrices == totalAmount

def test_incorrectDiscountCode(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    page.get_by_placeholder("Search for Vegetables and Fruits").fill("car")
    carrotProduct = page.locator(".product").filter(has_text="Carrot - 1 Kg")
    carrotProduct.get_by_role("button", name="ADD TO CART").click()
    page.locator("img[alt='Cart']").click()
    page.get_by_role("button", name="PROCEED TO CHECKOUT").click()
    page.get_by_placeholder("Enter promo code").fill("wrong code")
    page.get_by_role("button", name="Apply").click()
    expect(page.get_by_text("Invalid code ..!")).to_be_visible()


