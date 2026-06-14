from playwright.sync_api import Page, expect


def test_mockProducts(page: Page):

    mock_response = {"data":[],"message":"No Orders"}
    def mock_product(route):
        route.fulfill(
            json= mock_response
        )
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", mock_product)
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("fateme28ghasemi@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("F@teme78")
    page.get_by_role("button", name="Login").click()
    page.locator("button[routerlink='/dashboard/myorders']").click()

    # Assert that the order page does not contain any products
    expect(page.locator(".mt-4")).to_have_text(" You have No Orders to show at this time. Please Visit Back Us ")

