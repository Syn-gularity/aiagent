import os

def get_file_content(working_directory, file_path):
    #Setting up paths
    absolute_working_directory = os.path.abspath(working_directory)
    file = os.path.abspath(os.path.join(working_directory, file_path))
    #handling errorcases and limiting access
    if not(file.startswith(absolute_working_directory)):
        print(file)
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not(os.path.isfile(file)):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    #read-in of file
    MAX_CHARS = 10000
    try:
        with open(file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
    except Exception as e:
        return f"Error encountered: {e}"

    if len(file_content_string) > 9998:
        file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

    return file_content_string

