import time

from playwright.sync_api import Page, expect

def test_UIValidationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button", name="Add").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button", name="Add").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_validatePurchase(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button", name="Add").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button", name="Add").click()
    page.get_by_text("Checkout").click()
    page.get_by_role("button", name="Checkout").click()
    page.locator("#country").type("ira")
    page.locator("li").filter(has_text="Iran").click()
    page.get_by_role("button", name="Purchase").click()
    expect(page.get_by_text("Success! Thank you!")).to_be_visible()
    time.sleep(20)

