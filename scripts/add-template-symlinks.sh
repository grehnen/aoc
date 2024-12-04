if [ -z "$1" ]; then
  echo "Usage: $0 target_folder"
  exit 1
fi

target_folder=$1

# Ensure the target folder exists
if [ ! -d "$target_folder" ]; then
  echo "Target folder does not exist."
  exit 1
fi

# Get all files in the templates directory
template_files=$(find ./templates -type f)

# Create symbolic links for each file in the target folder
for file in $template_files; do
  link_path="$target_folder/$(basename $file)"
  ln -s "$file" "$link_path"
  echo "Created symlink: $link_path -> $file"
done