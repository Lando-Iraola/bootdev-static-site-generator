import unittest

from blocknode import BlockType, block_to_block_type


class TestBlockNode(unittest.TestCase):
    def test_is_paragraph(self):
        b_type = block_to_block_type("this is a normal paragraph")
        self.assertEqual(BlockType.PARAGRAPH, b_type)

    def test_is_heading(self):
        b_type = block_to_block_type("# this is a normal heading")
        self.assertEqual(BlockType.HEADING, b_type)

    def test_is_minimum_heading(self):
        b_type = block_to_block_type("###### this is a minimum heading")
        self.assertEqual(BlockType.HEADING, b_type)

    def test_is_no_longer_heading(self):
        b_type = block_to_block_type("####### this is not a heading")
        self.assertNotEqual(BlockType.HEADING, b_type)

    def test_is_quote(self):
        b_type = block_to_block_type("> this is a normal quote")
        self.assertEqual(BlockType.QUOTE, b_type)

    def test_is_quote_multiline(self):
        b_type = block_to_block_type("> this is a normal quote\n> more quote")
        self.assertEqual(BlockType.QUOTE, b_type)

    def test_is_not_quote_multiline(self):
        b_type = block_to_block_type("> this is a normal quote\n> more quote\nbroken")
        self.assertNotEqual(BlockType.QUOTE, b_type)

    def test_is_code(self):
        b_type = block_to_block_type("``` this is a normal quote ```")
        self.assertEqual(BlockType.CODE, b_type)

    def test_is_unordered_list(self):
        b_type = block_to_block_type("- this is an unordered list")
        self.assertEqual(BlockType.UNORDERED_LIST, b_type)

    def test_is_unordered_multiline(self):
        b_type = block_to_block_type(
            "- this is an unordered list\n- still a list\n- very much a list"
        )
        self.assertEqual(BlockType.UNORDERED_LIST, b_type)

    def test_is_not_unordered_multiline(self):
        b_type = block_to_block_type(
            "- this is an unordered list\n- still a list\n-no longer a list"
        )
        self.assertNotEqual(BlockType.UNORDERED_LIST, b_type)

    def test_is_ordered_list(self):
        b_type = block_to_block_type("1. this is an unordered list")
        self.assertEqual(BlockType.ORDERED_LIST, b_type)

    def test_is_ordered_list_multiple(self):
        b_type = block_to_block_type(
            "1. this is an unordered list\n2. still list and ordered\n3. very much an ordered list"
        )
        self.assertEqual(BlockType.ORDERED_LIST, b_type)

    def test_is_not_ordered_list_multiple(self):
        b_type = block_to_block_type(
            "1. this is an unordered list\n2 still list and ordered\n3. very much an ordered list"
        )
        self.assertNotEqual(BlockType.ORDERED_LIST, b_type)

    def test_is_not_ordered_list_by_wrong_number(self):
        b_type = block_to_block_type(
            "1. this is an unordered list\n3. still list and ordered\n2. very much an ordered list"
        )
        self.assertNotEqual(BlockType.ORDERED_LIST, b_type)

    def test_is_not_ordered_list_by_wrong_starting_number(self):
        b_type = block_to_block_type(
            "0. this is an unordered list\n1. still list and ordered\n2. very much an ordered list"
        )
        self.assertNotEqual(BlockType.ORDERED_LIST, b_type)


if __name__ == "__main__":
    unittest.main()
