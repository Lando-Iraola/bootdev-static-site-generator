import os
import sys
from copystatic import clear_directory, move_static_to_public_directory
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():

    base_path = sys.argv[1] or "/"
    clear_directory(dir_path_public)
    move_static_to_public_directory(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, base_path)


main()
