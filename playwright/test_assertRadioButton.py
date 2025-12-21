import time

from playwright.sync_api import Page, expect

def test_radioCounts(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(radios = page.locator(".radioButton")).to_have_count(3)

def test_radioVisibility(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    radios = page.locator(".radioButton")

    for i in range(radios.count()):
        expect(radios.nth(i)).to_be_visible()

def test_radioNotChecked(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    radios = page.locator(".radioButton")

    for j in range(radios.count()):
        expect(radios.nth(j)).not_to_be_checked()


def test_only_one_radio_can_be_selected(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    radios = page.locator(".radioButton")

    for i in range(radios.count()):
        radios.nth(i).click()
        expect(radios.nth(i)).to_be_checked()

        for j in range(radios.count()):
            if j != i:
                expect(radios.nth(j)).not_to_be_checked()
