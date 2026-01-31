import os
import shutil


def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)


def move_static_to_public_directory(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)

    contents = os.listdir(src)

    for item in contents:
        from_path = os.path.join(src, item)
        dest_path = os.path.join(dst, item)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isdir(from_path):
            move_static_to_public_directory(from_path, dest_path)
        else:

            shutil.copy(from_path, dest_path)
