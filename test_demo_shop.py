from time import sleep

import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser, have

LOGIN = "example1200@example.com"
PASSWORD = "123456"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"

def test_login():
    """Successful authorization to some demowebshop (UI)"""
    with step("Open login page"):
        browser.open("http://demowebshop.tricentis.com/login")

    with step("Fill login form"):
        browser.element("#Email").send_keys(LOGIN)
        browser.element("#Password").send_keys(PASSWORD).press_enter()

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))

def test_login_with_API():
    """Successful authorization to some demowebshop (UI)"""

    with step("Login with API"):
        request = requests.request("POST",
            url='https://demowebshop.tricentis.com/login',
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False)
    allure.attach(body=request.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
    allure.attach(body=str(request.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
    print(request.cookies)
    print(request.status_code)
    with step("Get cookie from API"):
      cookie = request.cookies.get("NOPCOMMERCE.AUTH")

    with step("Set cookie from API"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))
    sleep(5)