import time

from playwright.sync_api import Page, expect

def test_openNewTab(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#/")
    with page.expect_popup() as new_tab_info:
        page.get_by_text("Free Access to").click()
        new_tab = new_tab_info.value
        red_text = new_tab.locator(".red").text_content()
        splited_text = red_text.split("at")
        email = splited_text[1].split(" ")[1]
        assert email == "mentor@rahulshettyacademy.com"

def test_handleDialogBox(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()

def test_handleNewWindow(page: Page):
    page.goto("https://rahulshettyacademy.com/dropdownsPractise/")
    with page.expect_popup() as new_tab_info:
        page.locator(".blinkingText").click()
        new_tab = new_tab_info.value
        expect(new_tab).to_have_url("https://rahulshettyacademy.com/#/documents-request")

def test_openNewWindow(page: Page):
    page.goto("https://play1.automationcamp.ir/multi_window.html")
    