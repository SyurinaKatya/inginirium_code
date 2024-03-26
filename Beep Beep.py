
class Button:
    _click_count = 0

    def click(self):
        self._click_count += 1

    def click_count(self):
        return self._click_count

    def reset(self):
        self._click_count = 0


b1 = Button()
b2 = Button()

b1.click()
b1.click()
b2.click()