import time

from playwright.sync_api import Page, expect


# if input is visible or not 38
def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("#hide-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(5)


def test_acceptDialog(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)

def test_dismissDiolog(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)


def test_handleAlerts(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("#alertbtn").click()
    time.sleep(5)


def test_handle_newTab(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    with page.expect_popup() as newTabInfo:
        page.get_by_role("link", name="Open Tab").click()
        tabInfo = newTabInfo.value
        expect(tabInfo.get_by_role("link", name="Access all our Courses")).to_be_visible()
        time.sleep(5)
