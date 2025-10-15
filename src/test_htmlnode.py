import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            value="Testing",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        txt = node.props_to_html()

        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(txt, expected)

    def test_repr(self):
        node = HTMLNode(
            tag="a",
            value="Testing",
            props={"href": "https://www.google.com", "target": "_blank"},
        )

        expected = """tag=a
value=Testing
children=
props=
href:https://www.google.com
target:_blank"""
        txt = repr(node)

        self.assertEqual(txt, expected)

    def test_not_implemented_error(self):
        node = HTMLNode(
            tag="a",
            value="Testing",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
