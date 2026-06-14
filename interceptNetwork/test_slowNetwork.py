import time

from playwright.sync_api import Page, expect

def test_slowNetwork(page: Page):
    def slow_response(route):
        time.sleep(10)
        route.continue_()

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", slow_response)
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("fateme28ghasemi@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("F@teme78")
    page.get_by_role("button", name="Login").click()
    page.locator("button[routerlink='/dashboard/myorders']").click()

    # Assert that the loading spinner is displayed while the API response is delayed.
    expect(page.locator(".mt-4")).to_have_text(" Loading.... ")