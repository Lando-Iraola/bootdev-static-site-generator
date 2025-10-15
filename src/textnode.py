from enum import Enum


class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = None
        for t_p in TextType:
            if text_type == t_p.value:
                self.text_type = t_p
        self.url = url

    def __eq__(self, text_node):
        return (self.text == text_node.text and
                self.text_type == text_node.text_type and
                self.url == text_node.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value},  {self.url}"
