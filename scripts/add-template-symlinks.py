from os import path, symlink, remove, listdir, makedirs
import sys
import argparse


def create_symlinks(target_folder_name, force=False):
    script_dir = path.dirname(path.abspath(__file__))
    base_dir = path.join(script_dir, "..")

    # Ensure the target folder exists
    target_folder_path = path.abspath(path.join(base_dir, target_folder_name))
    if not path.isdir(target_folder_path):
        makedirs(target_folder_path)
        print(f"Created target folder: {target_folder_path}")

    # Get the templates
    template_dir = path.join(base_dir, "template")
    if not path.isdir(template_dir):
        print("Template directory does not exist.")
        sys.exit(1)

    template_files = [
        f
        for f in listdir(template_dir)
        if path.isfile(path.join(template_dir, f))
        and f not in [".gitignore", "template.py"]
    ]

    # Create symbolic links for each file in the target folder
    for file_name in template_files:
        removed = False
        source_path = path.abspath(path.join(template_dir, file_name))
        link_path = path.abspath(path.join(target_folder_path, file_name))
        if path.islink(link_path) and force:
            remove(link_path)
            removed = True
        try:
            symlink(source_path, link_path)
            if removed:
                print(f"Recreated symlink: {link_path} -> {source_path}")
            else:
                print(f"Created symlink: {link_path} -> {source_path}")
        except FileExistsError:
            print(f"Symlink already exists: {link_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create symlinks for template files.")
    parser.add_argument(
        "target_folder", help="The target folder to create symlinks in."
    )
    parser.add_argument(
        "-F",
        "--force",
        action="store_true",
        help="Remove and recreate existing symlinks.",
    )
    args = parser.parse_args()

    create_symlinks(args.target_folder, args.force)
