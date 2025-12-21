import time

from playwright.sync_api import Page, expect


# if input is visible or not 38
def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("#hide-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(5)

def test_handleAlert(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)