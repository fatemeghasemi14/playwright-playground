import time

from playwright.sync_api import Page, expect
from requests.packages import target


def test_validateSeleniumAlert(page: Page):
    page.goto("https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/mouseOver.html#")
    page.locator(".btnMouse").hover()
    page.on("alert", lambda alert: alert.accept())
    page.locator(".listener").filter(has_text="Selenium").click()

def test_validateRPAAlert(page: Page):
    page.goto("https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/mouseOver.html#")
    page.locator(".btnMouse").hover()
    with page.expect_popup() as alert_info:
        page.locator(".listener").filter(has_text="RPA").click()

    alert = alert_info.value
    alert.accept()


def test_dragAndDrop(page: Page):
    page.goto("https://play1.automationcamp.ir/mouse_events.html")
    # Locate Source And Target
    source = page.locator("#drag_source")
    target = page.locator("#drop_target")

    # Finding Coordinates Of Source And Target
    source_box = source.bounding_box()
    target_box = target.bounding_box()
    print(target_box)

    page.mouse.move(
        source_box["x"] + source_box["width"] / 2,
        source_box["y"] + source_box["height"] / 2
    )

    page.mouse.down()

    page.mouse.move(
        target_box["x"] + target_box["width"] / 2,
        target_box["y"] + target_box["height"] / 2
    )

    page.mouse.up()
    expect(target.locator("h3")).to_have_text("Drop is successful!")




