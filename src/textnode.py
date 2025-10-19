import re
from enum import Enum

from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = None
        for t_p in TextType:
            if text_type == t_p:
                self.text_type = t_p
        self.url = url

    def __eq__(self, text_node):
        return (
            self.text == text_node.text
            and self.text_type == text_node.text_type
            and self.url == text_node.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value},  {self.url}"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case _:
            raise ValueError("unknown text type")


def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            continue

        s_str = node.text.split(delimeter)
        for i in range(len(s_str)):
            if (i + 1) % 2 == 0:
                new_nodes.append(TextNode(s_str[i], text_type))
            elif s_str[i] != "":
                new_nodes.append(TextNode(s_str[i], TextType.TEXT))

    return new_nodes


def extract_markdown_images(text):
    first_pattern = r"(!\[.+?\])(\(.+?\))"
    second_pattern = r"(?<=!\[).*(?=\])|(?<=\().*(?=\))"
    matches = re.findall(first_pattern, text)
    list_of_tuples = []
    tuples = ()
    for match in matches:
        for text in match:
            tuples = tuples + (re.findall(second_pattern, text)[0],)
            if len(tuples) == 2:
                list_of_tuples.append(tuples)
                tuples = ()

    return list_of_tuples


def extract_markdown_links(text):
    first_pattern = r"(\[.+?\])(\(.+?\))"
    second_pattern = r"(?<=\[).*(?=\])|(?<=\().*(?=\))"
    matches = re.findall(first_pattern, text)
    list_of_tuples = []
    tuples = ()
    for match in matches:
        for text in match:
            tuples = tuples + (re.findall(second_pattern, text)[0],)
            if len(tuples) == 2:
                list_of_tuples.append(tuples)
                tuples = ()

    return list_of_tuples


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            continue

        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        delimeters = []
        for image in images:
            delimeters.append(f"![{image[0]}]({image[1]})")

        split_str = node.text

        for index, delimeter in enumerate(delimeters):
            if type(split_str) is list:
                split_str = split_str[index].split(delimeter, 1)
            else:
                split_str = split_str.split(delimeter, 1)

            for i, text in enumerate(split_str):
                if text == "":
                    new_nodes.append(
                        TextNode(images[index][0], TextType.IMAGE, images[index][1])
                    )
                    break

                new_nodes.append(TextNode(text, TextType.TEXT, None))
                new_nodes.append(
                    TextNode(images[index][0], TextType.IMAGE, images[index][1])
                )
                break

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            continue

        images = extract_markdown_links(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        delimeters = []
        for image in images:
            delimeters.append(f"[{image[0]}]({image[1]})")

        split_str = node.text

        for index, delimeter in enumerate(delimeters):
            if type(split_str) is list:
                split_str = split_str[index].split(delimeter, 1)
            else:
                split_str = split_str.split(delimeter, 1)

            for i, text in enumerate(split_str):
                if text == "":
                    new_nodes.append(
                        TextNode(images[index][0], TextType.LINK, images[index][1])
                    )
                    break

                new_nodes.append(TextNode(text, TextType.TEXT, None))
                new_nodes.append(
                    TextNode(images[index][0], TextType.LINK, images[index][1])
                )
                break

    return new_nodes
