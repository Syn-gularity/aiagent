import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    absolute_working_directory = os.path.abspath(working_directory)
    joined_directory = os.path.join(absolute_working_directory, directory)
    #print(joined_directory)
    #print(os.path.abspath(directory))
    #print(os.path.join(absolute_working_directory, directory))
    #print(os.path.isdir(os.path.join(absolute_working_directory, directory)))
    #print(os.path.isdir(os.path.abspath(directory)))
    if not(os.path.isdir(joined_directory)):
        return f'Error: "{directory}" is not a directory'
    if directory.startswith("..") or not(joined_directory.startswith(absolute_working_directory)):
         return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    listed_dir = os.listdir(joined_directory)
    ret_string=""
    for dat in listed_dir:
        filesize = os.path.getsize(joined_directory+"/"+dat)
        isdir = not os.path.isfile(joined_directory+"/"+dat)
        ret_string += f"{dat}: file_size={filesize} bytes, is_dir={isdir}\n"
        #print(os.path.getsize(joined_directory+"/"+dat))
    return ret_string

schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )