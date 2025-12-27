from playwright.sync_api import Playwright

ordersPayload = {"orders":[{"country":"Iran (Islamic Republic of)","productOrderedId":"68a961459320a140fe1ca57a"}]}
loginPayload = {"userEmail":"dummywebsite@rahulshettyacademy.com","userPassword":"Dummmy@@00"}

class ApiUtils:
    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url= "https://rahulshettyacademy.com", ignore_https_errors=True)
        response = api_request_context.post("/api/ecom/auth/login",
                                 data= loginPayload)
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]


    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url= "https://rahulshettyacademy.com", ignore_https_errors=True)
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data= ordersPayload,
                                 headers={"Authorization": token,
                                          "Content-Type": "application/json"})
        responseBody = response.json()
        return responseBody["orders"][0]