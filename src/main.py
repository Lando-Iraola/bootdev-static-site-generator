import os

from copystatic import clear_directory, move_static_to_public_directory
from markdown import generate_page

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
PUBLIC_FILES = os.path.join(PROJECT_ROOT, "public")
STATIC_FILES = os.path.join(PROJECT_ROOT, "static")
TEMPLATE_FILE = os.path.join(PROJECT_ROOT, "template.html")
MARKDOWN_FILE = os.path.join(PROJECT_ROOT, "contents", "index.md")


def main():
    clear_directory(PUBLIC_FILES)
    move_static_to_public_directory(STATIC_FILES, PUBLIC_FILES)
    generate_page(MARKDOWN_FILE, TEMPLATE_FILE, PUBLIC_FILES)


main()
