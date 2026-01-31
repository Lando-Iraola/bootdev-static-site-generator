from enum import Enum
from unittest import case

from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import ParentNode


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))

    return ParentNode("div", children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.OLIST:
            return olist_to_html_node(block)
        case BlockType.ULIST:
            return ulist_to_html_node(block)
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph_text = " ".join(lines)
    children = text_to_children(paragraph_text)
    return ParentNode("p", children)


def heading_to_html_node(block):
    heading_level = 0
    for c in block:
        if c == "#":
            heading_level += 1
        else:
            break
    text = block[heading_level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{heading_level}", children)


def code_to_html_node(block):
    lines = block.split("\n")
    inner_lines = lines[1:-1]
    text = "\n".join(inner_lines)
    if not text.endswith("\n"):
        text += "\n"
    child = text_node_to_html_node(TextNode(text, TextType.TEXT))
    holder = ParentNode("code", [child])
    return ParentNode("pre", [holder])


def olist_to_html_node(block):
    items = block.split("\n")
    list_items = []
    for item in items:
        children = text_to_children(item.split(".", 1)[1].strip())
        list_items.append(ParentNode("li", children))
    return ParentNode("ol", list_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    list_items = []
    for item in items:
        children = text_to_children(item[2:].strip())
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)



def quote_to_html_node(block):
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned = line.lstrip(">").strip()
        cleaned_lines.append(cleaned)
    content = " ".join(cleaned_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes
