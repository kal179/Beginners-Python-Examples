from cx_Freeze import setup, Executable

# file must be saved in same directory as the file you want to Compile
# Download cx_Freeze from source forge or run easy_install in power shell

nameOfExec = input("Name for Executable: ")
versionNumber = input("Version: ")
descript = input("Description: ")
filename = input("File to Compile(Add .py to file): ")

# run this file in cmd "python CompileFiles.py build"

setup(
    name = nameOfExec,
    version = versionNumber,
    description = descript,
    executables = [Executable(filename)]
    )