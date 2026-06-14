from playwright.sync_api import Page, expect

def test_handleShowAlertBotton(page: Page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")

    def handleAlertBotton(alert):
        alert.accept()

    page.on("alert", handleAlertBotton)
    page.get_by_role("button", name="Show Alert").click()
    expect(page.locator("#alert_handled_badge")).to_have_text("Alert handled")

