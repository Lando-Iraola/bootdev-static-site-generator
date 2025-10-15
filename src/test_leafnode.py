import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_raise_value_err(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()


if __name__ == "__main__":
    unittest.main()
