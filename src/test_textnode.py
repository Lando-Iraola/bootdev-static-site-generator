import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff(self):
        node = TextNode("this is a text node with different text",
                        TextType.LINKS, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_missing_url(self):
        node = TextNode("this is a text node with different text",
                        TextType.PLAIN)
        self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()
