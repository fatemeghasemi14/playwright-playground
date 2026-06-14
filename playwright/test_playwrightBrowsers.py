import time

from playwright.sync_api import Playwright, expect


def test_verifyCorrectCredentials(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/angularpractice/")
    page.locator("input[name='name']").first.fill("fghasemi")
    page.locator("input[name='email']").fill("fghasemi@gmail.com")
    page.get_by_label("Password").fill("fghasemi")
    page.locator("#exampleCheck1").check()
    page.get_by_role("combobox").select_option(label="Female")
    page.get_by_role("radio", name="Student").check()
    page.get_by_role("button", name="Submit").click()

# Verify That Entrepreneur Radio Button is disable
def test_disableRadioButton(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/angularpractice/")
    expect(page.get_by_role("radio", name="Entrepreneur")).not_to_be_enabled()



