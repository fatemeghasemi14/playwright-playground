import time

from playwright.sync_api import Page,Playwright, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")


#chromium headless mode, 1 single context
def test_playwrightShortcut(page: Page):
    page.goto("https://rahulshettyacademy.com/")


# cssSelector  #id .class
# Incorrect username/password.
def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning123")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)


# Empty username/password.
def test_firefoxBrowser(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("")
    page.get_by_label("Password:").fill("")
    page.get_by_role("combobox").select_option("Consultant")
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Empty username/password.")).to_be_visible()
    time.sleep(5)