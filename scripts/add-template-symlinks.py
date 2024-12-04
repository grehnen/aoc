import os
import sys


def create_symlinks(target_folder_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, "..")

    # Ensure the target folder exists
    target_folder_path = os.path.join(base_dir, target_folder_name)
    if not os.path.isdir(target_folder_path):
        print("Target folder does not exist.")
        sys.exit(1)

    # Get the templates
    template_dir = os.path.join(base_dir, "templates")
    if not os.path.isdir(template_dir):
        print("Templates directory does not exist.")
        sys.exit(1)

    template_files = [
        f
        for f in os.listdir(template_dir)
        if os.path.isfile(os.path.join(template_dir, f))
    ]

    # Create symbolic links for each file in the target folder
    for file_name in template_files:
        source_path = os.path.abspath(os.path.join(template_dir, file_name))
        link_path = os.path.abspath(os.path.join(target_folder_path, file_name))
        try:
            os.symlink(source_path, link_path)
            print(f"Created symlink: {link_path} -> {source_path}")
        except FileExistsError:
            print(f"Symlink already exists: {link_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_template_symlinks.py target_folder")
        sys.exit(1)

    target_folder = sys.argv[1]
    create_symlinks(target_folder)
