import os

# Specify the source file path
source_file = "/path/to/source/file.txt"

# Specify the new file name
new_file_name = "new_file.txt"

# Rename the file
os.rename(source_file, os.path.join(os.path.dirname(source_file), new_file_name))
