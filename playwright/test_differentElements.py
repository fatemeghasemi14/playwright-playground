import time

from playwright.sync_api import Page, expect

def test_verifyToolTipByTitle(page: Page):
    page.goto("https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/tooltip.html")
    expect(page.locator("#age")).to_have_attribute(name="title", value="Enter your Name")

def test_verifyToolTipMouseHover(page: Page):
    page.goto("https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/tooltip.html")
    page.locator("#age").hover()
    expect(page.get_by_role("tooltip")).to_have_text("Enter your Name")


def test_validateRating(page: Page):
    page.goto("https://play1.automationcamp.ir/advanced.html")
    ratingStar = page.evaluate("""
    () => {
    const el = document.querySelector('.star-rating');
    return window.getComputedStyle(el, '::after').content;
}
    """)
    ratingCount = ratingStar.count("*")
    page.locator("#txt_rating").fill("*" * ratingCount)
    page.locator("#check_rating").click()
    expect(page.locator("#validate_rating")).to_have_text("Well done!")


def test_mouseHover(page: Page):
    page.goto("https://play1.automationcamp.ir/mouse_events.html")
    page.get_by_role("button", name="Choose Language").hover()
    #choose python option and validate
    selectedOption = page.locator("#dd_python").text_content()
    page.locator("#dd_python").click()
    expect(page.locator("#hover_validate")).to_have_text(selectedOption)

def test_validateToolTipText(page: Page):
    page.goto("https://play2.automationcamp.ir/")
    page.locator(".tooltip").hover()
    expect(page.locator(".tooltiptext")).to_have_text("This is your sample Tooltip text")
