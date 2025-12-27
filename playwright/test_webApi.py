import time

from playwright.sync_api import Playwright
from utils.apiBase import ApiUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    api_utils = ApiUtils()
    orderId = api_utils.createOrder(playwright)
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("dummywebsite@rahulshettyacademy.com")
    page.get_by_placeholder("enter your passsword").fill("Dummmy@@00")
    page.get_by_role("button", name="Login").click()
    page.locator(".btn-custom").filter(has_text="ORDERS").click()
    row_information = page.locator("tr").filter(has_text=orderId)
    row_information.get_by_role("button", name="View").click()
    time.sleep(10)