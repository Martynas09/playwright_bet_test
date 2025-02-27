class Actions:
    def __init__(self, page):
        self.page = page
        self.iframe = page.frame_locator('#betgames_iframe')

    def click(self, data):
        self.iframe.locator(data).click()

    def wait(self, data):
        self.iframe.locator(data).wait_for(state='visible')

    def wait_for(self, data, amount):
        self.iframe.locator(data).wait_for(state='visible',timeout = amount)
    
    def get(self, data):
        return self.iframe.locator(data)

    def get_inner_text(self, data):
        return self.iframe.locator(data).inner_text()