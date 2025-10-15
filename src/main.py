from htmlnode import HTMLNode
from textnode import TextNode


def main():
    t = TextNode("some value", "link", "https://www.google.com")
    print(t)

    node = HTMLNode(
        tag="a",
        value="Testing",
        props={"href": "https://www.google.com", "target": "_blank"},
    )
    txt = node.props_to_html()
    print(node)


main()
