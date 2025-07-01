# from subdirectory.filename import function_name

# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python_file import run_python_file

#print(get_files_info("calculator","."))

#print(get_files_info("calculator","pkg"))

#print(get_files_info("calculator","/bin"))

#print(get_files_info("calculator","../"))

#print(get_file_content("calculator", "lorem.txt"))

# print("Test1:")
# print(get_file_content("calculator", "main.py"))

# print("Test2:")
# print(get_file_content("calculator", "pkg/calculator.py"))

# print("Test3:")
# print(get_file_content("calculator", "/bin/cat"))

# print("Test1:")
# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

# print("Test2:")
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

# print("Test3:")
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

print("Test1:")
print(run_python_file("calculator", "main.py"))

print("Test2:")
print(run_python_file("calculator", "tests.py"))

print("Test3:")
print(run_python_file("calculator", "../main.py"))

print("Test4:")
print(run_python_file("calculator", "nonexistent.py"))