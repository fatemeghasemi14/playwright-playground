from playwright.sync_api import Page, expect

def test_validateVisibleButton(page: Page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    page.get_by_role("button", name="Trigger").first.click()
    expect(page.get_by_role("button", name="Click Me")).to_be_visible()

def test_validateSpinnerDisappearation(page: Page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    page.locator("#invisibility_trigger").click()
    expect(page.get_by_role("status")).to_be_hidden()
    expect(page.locator("spinner_gone")).to_be_visible()


def test_validateClassAttributeChanged(page: Page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    page.locator("#enabled_trigger").click()
    expect(page.locator("#enabled_target")).to_have_attribute(name="class", value="btn btn-success")

def test_validateColorChanged(page: Page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    page.locator("#enabled_trigger").click()
    expect(page.locator("#enabled_target")).to_have_css(name="background-color", value="rgb(63, 182, 24)")

def test_validateTitleChanged(page: Page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    page.locator("#page_title_trigger").click()
    expect(page).to_have_title("My New Title!")

def test_validateInputValue(page: Page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    page.locator("#text_value_trigger").click()
    print(page.locator("#wait_for_value").input_value())
