from playwright.sync_api import Page

# if input is visible or not 38
def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_placeholder("Hide/Show Example")