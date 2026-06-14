from playwright.sync_api import Page, expect


def test_addToCartColorChanging(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("fateme28ghasemi@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("F@teme78")
    click_button = page.get_by_role("button", name="Login")
    click_button_box = click_button.bounding_box()
    page.mouse.click(
        click_button_box["x"] + click_button_box["width"] / 2,
        click_button_box["y"] + click_button_box["height"]/2,
    )

    add_to_cart_1 = page.get_by_role("button", name=" Add To Cart").nth(1)
    add_to_cart_1.hover()
    assert (add_to_cart_1.evaluate(
        "el => window.getComputedStyle(el).backgroundColor"
    )) == "rgb(150, 22, 31)"

