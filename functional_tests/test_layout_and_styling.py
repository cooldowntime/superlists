import os

from selenium.webdriver.common.keys import Keys

from .base import FunctionTest

MAX_WAIT = 10
os.environ['STAGING_SERVER'] = 'superlists-staging.xyz'


class LayoutAndStylingTest(FunctionTest):
    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=10
        )
        input_box.send_keys('哈哈哈')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: 哈哈哈')
        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=10
        )
