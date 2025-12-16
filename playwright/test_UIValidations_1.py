import time

from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Teacher")
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button", name="Add ").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button", name="Add ").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-object")).to_have_count(2)
    time.sleep(10)