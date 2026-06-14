from playwright.sync_api import Page, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")

def test_playwrightShortCut(page : Page):
    page.goto("https://rahulshettyacademy.com/")
    time.sleep(10)

""" Give Correct Credentials And
    Verify That You Can Sign In Or Not"""
def test_coreLocators(page : Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")

    # Select Option By Value
    page.get_by_role("combobox").select_option("teach")

    # Select Option By Lable
    page.get_by_role("combobox").select_option(label="Consultant")

    # css selector #id, .class, tag name
    page.locator("#terms").check()

    page.get_by_role("button", name="Sign In").click()


""" Give Wrong Credentials And
Verify That You Give proper error message"""
def test_wrongCredentials(page : Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("#username").fill("fghasemi")
    page.locator("#password").fill("fghasemi")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
