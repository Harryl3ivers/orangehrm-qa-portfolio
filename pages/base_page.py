from playwright.sync_api import expect
class BasePage:
    def __init__(self,page):
        self.page = page

    def navigate(self,url):
        self.page.goto(url)

    def click(self, selector):
        element = self.page.locator(selector)
        element.wait_for(state="visible", timeout=5000)
        element.click(timeout=10000)


    def fill(self, selector, text):
        element = self.page.locator(selector)
        element.fill(text, timeout=5000)


    def get_text(self, selector):
        element = self.page.locator(selector)
        expect(element).to_be_visible(timeout=5000)
        return element.text_content()

    def is_visible(self,selector):
        element = self.page.locator(selector)
        expect(element).to_be_visible(timeout=5000)
        return element.is_visible() 