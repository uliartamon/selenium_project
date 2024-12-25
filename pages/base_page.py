class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = self.url

    def open(self):
        self.browser.get(self.url)