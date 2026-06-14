import time

from playwright.sync_api import Page, expect

def test_inputVisibility(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_visible()

def test_elementAbility(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.locator("input[value='radio1']")).to_be_enabled()
    page.locator("input[value='radio1']").check()
    expect(page.locator("input[value='radio1']")).to_be_checked()

def test_elementEmptieness(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_placeholder("Enter Your Name").fill("fateme")
    page.get_by_placeholder("Enter Your Name").clear()
    expect(page.get_by_placeholder("Enter Your Name")).to_be_empty()

