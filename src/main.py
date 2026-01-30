import os
from copystatic import clear_directory, move_static_to_public_directory

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
PUBLIC_FILES = os.path.join(PROJECT_ROOT, "public")
STATIC_FILES = os.path.join(PROJECT_ROOT, "static")


def main():
    clear_directory(PUBLIC_FILES)
    move_static_to_public_directory(STATIC_FILES, PUBLIC_FILES)


main()
