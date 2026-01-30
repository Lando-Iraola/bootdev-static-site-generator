import os
import shutil




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