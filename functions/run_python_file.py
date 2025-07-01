import os
import subprocess

def run_python_file(working_directory, file_path):
    #Setting up paths
    absolute_working_directory = os.path.abspath(working_directory)
    file = os.path.abspath(os.path.join(working_directory, file_path))
    #handling errorcases and limiting access
    if not(file.startswith(absolute_working_directory)):
        print(file)
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not(os.path.exists(file)):
        return f'Error: File "{file_path}" not found.'
    if file[-2:]!="py":
        return f'Error: "{file_path}" is not a Python file.'

    #running the file for max30s and capturing all the output
    result = subprocess.run(["python3", file], capture_output=True, text=True, timeout=30)
    ret_string=""
    ret_string += f"STDOUT: {result.stdout}\n"
    ret_string += f"STDERR: {result.stderr}\n"
    if ret_string == "":
        return "No output produced."
    if result.returncode!=0:
        ret_string += f"Process exited with code {result.returncode}\n"
    return ret_string