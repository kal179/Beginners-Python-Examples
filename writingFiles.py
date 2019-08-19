# Writing to a file in a directory
from pathlib import Path

#check if valid directory
while True:
    try:
        d = str(input('Please enter a directory path: '))
        d_path = Path(d)
        if d_path.is_dir():
            break
        else:
            raise ValueError
    except (ValueError, OSError):
        print('Specified directory path not found')

#show all files in directory chosen
lst = []
for obj in d_path.iterdir():
    if obj.is_file():
        lst.append(obj)
# sorting lexicographically taking each path object as a string
lst_copy = sorted(lst, key=lambda obj: str(obj))
for obj in lst_copy:
    print(obj)

#open file
while True:
    try:
        file = str(input('Please enter a file name: '))
        fileToWrite = open(file, 'w') # 'w' writes to the file
        textToWrite = str(input('Text to write: '))
        fileToWrite.write(textToWrite) # writing file
        fileToWrite.close() # closing the file
    except (OSError, FileNotFoundError):
        print('File error')

