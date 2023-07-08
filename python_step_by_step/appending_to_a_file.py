# Open the file in append mode
file_path = "/path/to/existing_file.txt"
content = "This is the content to be appended."

with open(file_path, "a") as file:
    file.write(content)
