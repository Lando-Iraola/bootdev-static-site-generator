import os
import shutil

from textnode import TextNode, TextType

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
PUBLIC_FILES = os.path.join(PROJECT_ROOT, "public")
STATIC_FILES = os.path.join(PROJECT_ROOT, "static")


def clear_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
        return
    contents = os.listdir(directory)
    for item in contents:
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
        else:
            os.remove(full_path)
    return


def move_static_to_public_directory(src, dst, cleaned=False):
    if not cleaned:
        clear_directory(dst)
        cleaned = True
    contents = os.listdir(src)

    for item in contents:
        path = os.path.join(src, item)
        if os.path.isdir(path):
            new_directory = os.path.join(dst, item)
            os.mkdir(new_directory)
            move_static_to_public_directory(path, new_directory, cleaned=cleaned)
        else:
            copy_to = os.path.join(dst, item)
            shutil.copy(path, copy_to)




def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)
    move_static_to_public_directory(STATIC_FILES, PUBLIC_FILES)


main()
