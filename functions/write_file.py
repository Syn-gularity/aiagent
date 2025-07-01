import os

def write_file(working_directory, file_path, content):
    #Setting up paths
    absolute_working_directory = os.path.abspath(working_directory)
    file = os.path.abspath(os.path.join(working_directory, file_path))
    #handling errorcases and limiting access
    if not(file.startswith(absolute_working_directory)):
        print(file)
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    #if file_path doesn't exist, create it
    if not(os.path.exists(os.path.dirname(file))):
        print("folder exists" + os.path.dirname(file))
        os.makedirs(os.path.dirname(file))
    #overwrite the file content with content
    try:
        with open(file, "w+") as f:
            f.write(content)
    except Exception as e:
        return f"Error encountered: {e}"

    ret_string = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    return ret_string