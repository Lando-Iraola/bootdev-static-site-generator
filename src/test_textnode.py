import unittest

from textnode import TextNode, TextType, split_nodes_delimiter, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff(self):
        node = TextNode(
            "this is a text node with different text",
            TextType.LINKS,
            "https://www.google.com",
        )
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_missing_url(self):
        node = TextNode("this is a text node with different text", TextType.TEXT)
        self.assertEqual(node.url, None)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic_delimiter(self):
        node = TextNode(
            "This is a text node _with italics in between!_ its contents", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is a text node ", TextType.TEXT),
            TextNode("with italics in between!", TextType.ITALIC),
            TextNode(" its contents", TextType.TEXT),
        ]
        self.assertEqual(repr(new_nodes), repr(expected_nodes))

    def test_italic_delimiter_text_after_delimeter(self):
        node = TextNode("This is a text node _with italics in between!_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)


if __name__ == "__main__":
    unittest.main()
