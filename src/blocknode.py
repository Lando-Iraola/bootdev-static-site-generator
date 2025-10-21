from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_block):
    if markdown_block[:3] == "```" and markdown_block[-3:] == "```":
        return BlockType.CODE

    if markdown_block[0] == ">":
        split_block = markdown_block.split("\n")
        is_quote = True
        for line in split_block:
            if line[0] != ">":
                is_quote = False

        if is_quote:
            return BlockType.QUOTE

    if markdown_block[0] == "#":
        count = 0
        is_heading = True
        for index, char in enumerate(markdown_block[:7]):
            if char == "#":
                count += 1
            if char != "#" and markdown_block[index - 1] == "#" and char != " ":
                is_heading = False
        if count > 6:
            is_heading = False
        if is_heading:
            return BlockType.HEADING

    if markdown_block[0] == "-":
        split_block = markdown_block.split("\n")
        is_list = True
        for line in split_block:
            if line[0] != "-":
                is_list = False
            if len(line) == 1 or line[1] != " ":
                is_list = False
        if is_list:
            return BlockType.UNORDERED_LIST

    if markdown_block[0].isdigit():
        split_block = markdown_block.split("\n")
        is_list = True
        previous_number = 0
        for line in split_block:
            if not line[0].isdigit():
                is_list = False
            if len(line) == 1:
                is_list = False

            for index, char in enumerate(line):
                if not char.isdigit() and char != ".":
                    is_list = False
                    break
                if not char.isdigit() and char == "." and len(line) <= index + 1:
                    is_list = False
                    break
                if not char.isdigit() and char == "." and line[index + 1] != " ":
                    is_list = False
                    break
                if not char.isdigit() and char == "." and line[index + 1] == " ":
                    if int(previous_number) + 1 != int(line[:index]):
                        is_list = False
                        break
                    previous_number = line[:index]
                    break

        if is_list:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
