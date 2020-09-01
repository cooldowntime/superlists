from unittest import skip

from .base import FunctionTest


class ItemValidationTest(FunctionTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        self.fail('write me!')
